import asyncio
import logging
import os
from aiohttp import web
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    PicklePersistence,
    filters,
)
from telegram.constants import ParseMode

from config import BOT_TOKEN, ADMIN_ID

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

SETUP_MSG, SETUP_CHAT, SETUP_FREQ, SETUP_FREQ_CUSTOM, SETUP_CONFIRM = range(5)


def is_admin(uid: int) -> bool:
    return uid == ADMIN_ID


def _is_running(ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    return bool(ctx.job_queue.get_jobs_by_name("cargo"))


def _panel_keyboard(active: bool) -> InlineKeyboardMarkup:
    toggle = (
        InlineKeyboardButton("⏹ Остановить", callback_data="panel_stop")
        if active
        else InlineKeyboardButton("▶️ Запустить", callback_data="panel_start")
    )
    return InlineKeyboardMarkup([
        [toggle],
        [InlineKeyboardButton("⚙️ Настроить заново", callback_data="panel_setup")],
        [InlineKeyboardButton("📊 Обновить статус",   callback_data="panel_status")],
    ])


def _settings_summary(bd: dict) -> str:
    text     = bd.get("cargo_text", "—")
    chat     = bd.get("target_chat", "—")
    freq     = bd.get("freq", 1)
    interval = round(60 / freq, 1)
    return (
        f"📍 Канал/группа: `{chat}`\n"
        f"⏱ Частота: {freq} раз/мин (каждые {interval} сек)\n\n"
        f"📝 *Сообщение:*\n{text}"
    )


# ── /start — control panel ────────────────────────────────────────────────────

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("🚛 Cargo Bot")
        return
    bd = ctx.bot_data
    if not bd.get("cargo_text"):
        await update.message.reply_text(
            "🚛 *Cargo Auto-Poster*\n\n"
            "Ещё не настроено. Используйте /setup.",
            parse_mode=ParseMode.MARKDOWN,
        )
        return
    active = _is_running(ctx)
    status = "🟢 Работает" if active else "🔴 Остановлена"
    await update.message.reply_text(
        f"🚛 *Cargo Auto-Poster*\n\n📡 Статус: {status}\n\n" + _settings_summary(bd),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_panel_keyboard(active),
    )


# ── /chatid — helper ──────────────────────────────────────────────────────────

async def cmd_chatid(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Chat ID: `{update.effective_chat.id}`",
        parse_mode=ParseMode.MARKDOWN,
    )


# ── Job: post to channel ──────────────────────────────────────────────────────

async def _post_cargo(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    bd      = ctx.bot_data
    text    = bd.get("cargo_text", "")
    chat_id = bd.get("target_chat", "")
    if not text or not chat_id:
        return
    try:
        await ctx.bot.send_message(chat_id=chat_id, text=text)
        logger.info("Posted to %s", chat_id)
    except Exception as e:
        logger.error("Post failed: %s", e)


# ── Panel button handler ──────────────────────────────────────────────────────

async def panel_btn(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if not is_admin(query.from_user.id):
        return
    bd = ctx.bot_data

    if query.data == "panel_start":
        if not bd.get("cargo_text") or not bd.get("target_chat"):
            await query.answer("⚠️ Сначала настройте /setup", show_alert=True)
            return
        if not _is_running(ctx):
            freq     = bd.get("freq", 1)
            interval = 60 / freq
            ctx.job_queue.run_repeating(_post_cargo, interval=interval, first=0, name="cargo")
        bd["posting_active"] = True
        await query.edit_message_text(
            "🚛 *Cargo Auto-Poster*\n\n✅ Рассылка запущена!\n\n" + _settings_summary(bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(True),
        )

    elif query.data == "panel_stop":
        for job in ctx.job_queue.get_jobs_by_name("cargo"):
            job.schedule_removal()
        bd["posting_active"] = False
        await query.edit_message_text(
            "🚛 *Cargo Auto-Poster*\n\n⏹ Рассылка остановлена.\n\n" + _settings_summary(bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(False),
        )

    elif query.data == "panel_status":
        active = _is_running(ctx)
        status = "🟢 Работает" if active else "🔴 Остановлена"
        await query.edit_message_text(
            f"🚛 *Cargo Auto-Poster*\n\n📡 Статус: {status}\n\n" + _settings_summary(bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(active),
        )


# ── Setup conversation ────────────────────────────────────────────────────────

async def setup_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    ctx.user_data["setup"] = {}
    text = (
        "⚙️ *Настройка авторассылки*\n\n"
        "📝 *Шаг 1 / 3*\n\n"
        "Отправьте текст объявления:"
    )
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
    return SETUP_MSG


async def setup_got_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["setup"]["text"] = update.message.text
    await update.message.reply_text(
        "📍 *Шаг 2 / 3*\n\n"
        "Укажите *Chat ID* группы или канала.\n\n"
        "Как узнать ID:\n"
        "1. Добавьте бота в группу/канал\n"
        "2. Напишите там `/chatid`\n"
        "3. Скопируйте число и отправьте сюда\n\n"
        "_Для канала ID начинается с `-100`_",
        parse_mode=ParseMode.MARKDOWN,
    )
    return SETUP_CHAT


async def setup_got_chat(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if update.message.forward_from_chat:
        chat_id = str(update.message.forward_from_chat.id)
    else:
        raw = update.message.text.strip()
        if not raw.lstrip("-").isdigit():
            await update.message.reply_text(
                "❌ Неверный формат. Отправьте числовой Chat ID.\n"
                "Пример: `-1001234567890`",
                parse_mode=ParseMode.MARKDOWN,
            )
            return SETUP_CHAT
        chat_id = raw

    ctx.user_data["setup"]["chat_id"] = chat_id
    await update.message.reply_text(
        "⏱ *Шаг 3 / 3*\n\nСколько раз в минуту отправлять?",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("1 раз/мин",  callback_data="freq_1"),
                InlineKeyboardButton("2 раза/мин", callback_data="freq_2"),
            ],
            [
                InlineKeyboardButton("3 раза/мин", callback_data="freq_3"),
                InlineKeyboardButton("4 раза/мин", callback_data="freq_4"),
            ],
            [InlineKeyboardButton("✏️ Другое число", callback_data="freq_custom")],
        ]),
    )
    return SETUP_FREQ


async def setup_freq_btn(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    if query.data == "freq_custom":
        await query.edit_message_text("✏️ Введите число раз в минуту (1 – 60):")
        return SETUP_FREQ_CUSTOM
    freq = int(query.data.split("_")[1])
    ctx.user_data["setup"]["freq"] = freq
    await query.edit_message_text("⏳")
    return await _show_preview(query.message, ctx)


async def setup_freq_custom(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        freq = int(update.message.text.strip())
        if not (1 <= freq <= 60):
            raise ValueError
    except ValueError:
        await update.message.reply_text("❌ Введите целое число от 1 до 60.")
        return SETUP_FREQ_CUSTOM
    ctx.user_data["setup"]["freq"] = freq
    return await _show_preview(update.message, ctx)


async def _show_preview(message, ctx) -> int:
    s        = ctx.user_data["setup"]
    freq     = s["freq"]
    interval = round(60 / freq, 1)
    await message.reply_text(
        f"👁 *Предпросмотр:*\n\n"
        f"📍 Канал/группа: `{s['chat_id']}`\n"
        f"⏱ {freq} раз/мин (каждые {interval} сек)\n\n"
        f"📝 *Сообщение:*\n{s['text']}",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("✅ Запустить", callback_data="setup_confirm"),
            InlineKeyboardButton("❌ Отмена",    callback_data="setup_cancel"),
        ]]),
    )
    return SETUP_CONFIRM


async def setup_confirm(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    s  = ctx.user_data.get("setup", {})
    bd = ctx.bot_data
    bd["cargo_text"]     = s["text"]
    bd["target_chat"]    = s["chat_id"]
    bd["freq"]           = s["freq"]
    bd["posting_active"] = True

    for job in ctx.job_queue.get_jobs_by_name("cargo"):
        job.schedule_removal()
    ctx.job_queue.run_repeating(
        _post_cargo, interval=60 / s["freq"], first=0, name="cargo"
    )
    ctx.user_data["setup"] = {}
    await query.edit_message_text(
        "✅ *Рассылка запущена!*\n\n" + _settings_summary(bd),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_panel_keyboard(True),
    )
    return ConversationHandler.END


async def setup_cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["setup"] = {}
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text("❌ Настройка отменена.")
    else:
        await update.message.reply_text("❌ Настройка отменена.")
    return ConversationHandler.END


# ── Health check & run ────────────────────────────────────────────────────────

async def _health(request):
    return web.Response(text="OK")


async def _run(app: Application) -> None:
    port = int(os.getenv("PORT", 8080))
    web_app = web.Application()
    web_app.router.add_get("/", _health)
    runner = web.AppRunner(web_app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
    logger.info("Health server on port %s", port)

    async with app:
        await app.start()
        bd = app.bot_data
        if bd.get("posting_active") and bd.get("cargo_text") and bd.get("target_chat"):
            freq = bd.get("freq", 1)
            app.job_queue.run_repeating(
                _post_cargo, interval=60 / freq, first=5, name="cargo"
            )
            logger.info("Resumed posting → %s (%s/min)", bd["target_chat"], freq)
        await app.updater.start_polling(drop_pending_updates=True)
        await asyncio.Event().wait()


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN not set")

    persistence = PicklePersistence(filepath="bot_data.pkl")
    app = Application.builder().token(BOT_TOKEN).persistence(persistence).build()

    setup_conv = ConversationHandler(
        entry_points=[
            CommandHandler("setup", setup_start),
            CallbackQueryHandler(setup_start, pattern="^panel_setup$"),
        ],
        states={
            SETUP_MSG:         [MessageHandler(filters.TEXT & ~filters.COMMAND, setup_got_msg)],
            SETUP_CHAT:        [MessageHandler(filters.ALL & ~filters.COMMAND, setup_got_chat)],
            SETUP_FREQ:        [CallbackQueryHandler(setup_freq_btn, pattern="^freq_")],
            SETUP_FREQ_CUSTOM: [MessageHandler(filters.TEXT & ~filters.COMMAND, setup_freq_custom)],
            SETUP_CONFIRM:     [
                CallbackQueryHandler(setup_confirm, pattern="^setup_confirm$"),
                CallbackQueryHandler(setup_cancel,  pattern="^setup_cancel$"),
            ],
        },
        fallbacks=[CommandHandler("cancel", setup_cancel)],
        per_message=False,
    )

    app.add_handler(CommandHandler("start",  cmd_start))
    app.add_handler(CommandHandler("chatid", cmd_chatid))
    app.add_handler(setup_conv)
    app.add_handler(CallbackQueryHandler(panel_btn, pattern="^panel_"))

    logger.info("Cargo bot started")
    asyncio.run(_run(app))


if __name__ == "__main__":
    main()
