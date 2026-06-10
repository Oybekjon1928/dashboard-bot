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

LANG_PICK = 0
SETUP_MSG, SETUP_CHAT, SETUP_FREQ, SETUP_FREQ_CUSTOM, SETUP_CONFIRM = range(1, 6)

# ── Texts ─────────────────────────────────────────────────────────────────────

TEXTS = {
    "ru": {
        "not_admin":       "🚛 Cargo Bot",
        "not_configured":  "🚛 *Cargo Auto-Poster*\n\nЕщё не настроено. Используйте /setup.",
        "panel_header":    "🚛 *Cargo Auto-Poster*",
        "status_label":    "📡 Статус",
        "running":         "🟢 Работает",
        "stopped":         "🔴 Остановлена",
        "chat_label":      "📍 Канал/группа",
        "freq_label":      "⏱ Частота",
        "freq_value":      "{freq} раз/мин (каждые {interval} сек)",
        "msg_label":       "📝 *Сообщение:*",
        "btn_stop":        "⏹ Остановить",
        "btn_start":       "▶️ Запустить",
        "btn_setup":       "⚙️ Настроить заново",
        "btn_status":      "📊 Обновить статус",
        "btn_lang":        "🌐 O'zbek",
        "started":         "✅ Рассылка запущена!",
        "stopped_msg":     "⏹ Рассылка остановлена.",
        "no_settings":     "⚠️ Сначала настройте /setup",
        "setup_step1": (
            "⚙️ *Настройка авторассылки*\n\n"
            "📝 *Шаг 1 / 3*\n\n"
            "Отправьте текст объявления:"
        ),
        "setup_step2": (
            "📍 *Шаг 2 / 3*\n\n"
            "Укажите *Chat ID* группы или канала.\n\n"
            "Как узнать ID:\n"
            "1. Добавьте бота в группу/канал\n"
            "2. Напишите там `/chatid`\n"
            "3. Скопируйте число и отправьте сюда\n\n"
            "_Для канала ID начинается с `-100`_"
        ),
        "setup_step3":     "⏱ *Шаг 3 / 3*\n\nСколько раз в минуту отправлять?",
        "freq_1":          "1 раз/мин",
        "freq_2":          "2 раза/мин",
        "freq_3":          "3 раза/мин",
        "freq_4":          "4 раза/мин",
        "freq_custom_btn": "✏️ Другое число",
        "freq_custom_ask": "✏️ Введите число раз в минуту (1 – 60):",
        "freq_invalid":    "❌ Введите целое число от 1 до 60.",
        "preview": (
            "👁 *Предпросмотр:*\n\n"
            "📍 Канал/группа: `{chat}`\n"
            "⏱ {freq} раз/мин (каждые {interval} сек)\n\n"
            "📝 *Сообщение:*\n{text}"
        ),
        "btn_confirm":     "✅ Запустить",
        "btn_cancel":      "❌ Отмена",
        "cancelled":       "❌ Настройка отменена.",
        "chat_invalid":    "❌ Неверный формат. Отправьте числовой Chat ID.\nПример: `-1001234567890`",
        "lang_select":     "🌐 Выберите язык / Tilni tanlang:",
    },
    "uz": {
        "not_admin":       "🚛 Yuk Boti",
        "not_configured":  "🚛 *Yuk Avto-Jo'natuvchi*\n\nHali sozlanmagan. /setup dan foydalaning.",
        "panel_header":    "🚛 *Yuk Avto-Jo'natuvchi*",
        "status_label":    "📡 Holat",
        "running":         "🟢 Ishlaydi",
        "stopped":         "🔴 To'xtatildi",
        "chat_label":      "📍 Kanal/guruh",
        "freq_label":      "⏱ Tezlik",
        "freq_value":      "{freq} marta/daq (har {interval} son)",
        "msg_label":       "📝 *Xabar:*",
        "btn_stop":        "⏹ To'xtatish",
        "btn_start":       "▶️ Boshlash",
        "btn_setup":       "⚙️ Qayta sozlash",
        "btn_status":      "📊 Holatni yangilash",
        "btn_lang":        "🌐 Русский",
        "started":         "✅ Yuborish boshlandi!",
        "stopped_msg":     "⏹ Yuborish to'xtatildi.",
        "no_settings":     "⚠️ Avval /setup orqali sozlang",
        "setup_step1": (
            "⚙️ *Avtoyuborish sozlamasi*\n\n"
            "📝 *Qadam 1 / 3*\n\n"
            "E'lon matnini yuboring:"
        ),
        "setup_step2": (
            "📍 *Qadam 2 / 3*\n\n"
            "Guruh yoki kanal *Chat ID* sini kiriting.\n\n"
            "ID ni qanday bilish:\n"
            "1. Botni guruh/kanalga qo'shing\n"
            "2. U yerda `/chatid` yozing\n"
            "3. Raqamni nusxa oling va shu yerga yuboring\n\n"
            "_Kanal uchun ID `-100` bilan boshlanadi_"
        ),
        "setup_step3":     "⏱ *Qadam 3 / 3*\n\nDaqiqada necha marta yuborish?",
        "freq_1":          "1 marta/daq",
        "freq_2":          "2 marta/daq",
        "freq_3":          "3 marta/daq",
        "freq_4":          "4 marta/daq",
        "freq_custom_btn": "✏️ Boshqa raqam",
        "freq_custom_ask": "✏️ Daqiqada necha marta yuborishni kiriting (1 – 60):",
        "freq_invalid":    "❌ 1 dan 60 gacha butun son kiriting.",
        "preview": (
            "👁 *Ko'rinish:*\n\n"
            "📍 Kanal/guruh: `{chat}`\n"
            "⏱ {freq} marta/daq (har {interval} son)\n\n"
            "📝 *Xabar:*\n{text}"
        ),
        "btn_confirm":     "✅ Boshlash",
        "btn_cancel":      "❌ Bekor",
        "cancelled":       "❌ Sozlash bekor qilindi.",
        "chat_invalid":    "❌ Noto'g'ri format. Raqamli Chat ID yuboring.\nMisol: `-1001234567890`",
        "lang_select":     "🌐 Выберите язык / Tilni tanlang:",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["ru"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def get_lang(ctx: ContextTypes.DEFAULT_TYPE) -> str:
    return ctx.user_data.get("lang", "ru")


def is_admin(uid: int) -> bool:
    return uid == ADMIN_ID


def _is_running(ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    return bool(ctx.job_queue.get_jobs_by_name("cargo"))


def _panel_keyboard(lang: str, active: bool) -> InlineKeyboardMarkup:
    toggle = (
        InlineKeyboardButton(t(lang, "btn_stop"), callback_data="panel_stop")
        if active
        else InlineKeyboardButton(t(lang, "btn_start"), callback_data="panel_start")
    )
    return InlineKeyboardMarkup([
        [toggle],
        [InlineKeyboardButton(t(lang, "btn_setup"),  callback_data="panel_setup")],
        [InlineKeyboardButton(t(lang, "btn_status"), callback_data="panel_status")],
        [InlineKeyboardButton(t(lang, "btn_lang"),   callback_data="panel_lang")],
    ])


def _settings_summary(lang: str, bd: dict) -> str:
    text     = bd.get("cargo_text", "—")
    chat     = bd.get("target_chat", "—")
    freq     = bd.get("freq", 1)
    interval = round(60 / freq, 1)
    return (
        f"{t(lang, 'chat_label')}: `{chat}`\n"
        f"{t(lang, 'freq_label')}: {t(lang, 'freq_value', freq=freq, interval=interval)}\n\n"
        f"{t(lang, 'msg_label')}\n{text}"
    )


# ── /start ────────────────────────────────────────────────────────────────────

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        await update.message.reply_text(t("ru", "not_admin"))
        return ConversationHandler.END

    if "lang" not in ctx.user_data:
        await update.message.reply_text(
            t("ru", "lang_select"),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🇷🇺 Русский", callback_data="setlang_ru"),
                InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="setlang_uz"),
            ]]),
        )
        return LANG_PICK

    await _send_panel(update.message, ctx)
    return ConversationHandler.END


async def lang_picked(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    ctx.user_data["lang"] = "uz" if query.data == "setlang_uz" else "ru"
    await query.edit_message_text("✅")
    await _send_panel(query.message, ctx)
    return ConversationHandler.END


async def _send_panel(message, ctx) -> None:
    lang   = get_lang(ctx)
    bd     = ctx.bot_data
    active = _is_running(ctx)
    status = t(lang, "running") if active else t(lang, "stopped")

    if not bd.get("cargo_text"):
        await message.reply_text(t(lang, "not_configured"), parse_mode=ParseMode.MARKDOWN)
        return

    await message.reply_text(
        f"{t(lang, 'panel_header')}\n\n"
        f"{t(lang, 'status_label')}: {status}\n\n"
        + _settings_summary(lang, bd),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_panel_keyboard(lang, active),
    )


# ── /chatid ───────────────────────────────────────────────────────────────────

async def cmd_chatid(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Chat ID: `{update.effective_chat.id}`",
        parse_mode=ParseMode.MARKDOWN,
    )


# ── Job ───────────────────────────────────────────────────────────────────────

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


# ── Panel buttons ─────────────────────────────────────────────────────────────

async def panel_btn(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if not is_admin(query.from_user.id):
        return
    lang = get_lang(ctx)
    bd   = ctx.bot_data

    if query.data == "panel_lang":
        new_lang = "uz" if lang == "ru" else "ru"
        ctx.user_data["lang"] = new_lang
        lang = new_lang
        active = _is_running(ctx)
        status = t(lang, "running") if active else t(lang, "stopped")
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n"
            f"{t(lang, 'status_label')}: {status}\n\n"
            + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, active),
        )
        return

    if query.data == "panel_start":
        if not bd.get("cargo_text") or not bd.get("target_chat"):
            await query.answer(t(lang, "no_settings"), show_alert=True)
            return
        if not _is_running(ctx):
            ctx.job_queue.run_repeating(
                _post_cargo, interval=60 / bd.get("freq", 1), first=0, name="cargo"
            )
        bd["posting_active"] = True
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'started')}\n\n"
            + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, True),
        )

    elif query.data == "panel_stop":
        for job in ctx.job_queue.get_jobs_by_name("cargo"):
            job.schedule_removal()
        bd["posting_active"] = False
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'stopped_msg')}\n\n"
            + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, False),
        )

    elif query.data == "panel_status":
        active = _is_running(ctx)
        status = t(lang, "running") if active else t(lang, "stopped")
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n"
            f"{t(lang, 'status_label')}: {status}\n\n"
            + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, active),
        )


# ── Setup conversation ────────────────────────────────────────────────────────

async def setup_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    lang = get_lang(ctx)
    ctx.user_data["setup"] = {}
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            t(lang, "setup_step1"), parse_mode=ParseMode.MARKDOWN
        )
    else:
        await update.message.reply_text(
            t(lang, "setup_step1"), parse_mode=ParseMode.MARKDOWN
        )
    return SETUP_MSG


async def setup_got_msg(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["setup"]["text"] = update.message.text
    await update.message.reply_text(t(lang, "setup_step2"), parse_mode=ParseMode.MARKDOWN)
    return SETUP_CHAT


async def setup_got_chat(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    if update.message.forward_from_chat:
        chat_id = str(update.message.forward_from_chat.id)
    else:
        raw = update.message.text.strip()
        if not raw.lstrip("-").isdigit():
            await update.message.reply_text(
                t(lang, "chat_invalid"), parse_mode=ParseMode.MARKDOWN
            )
            return SETUP_CHAT
        chat_id = raw

    ctx.user_data["setup"]["chat_id"] = chat_id
    await update.message.reply_text(
        t(lang, "setup_step3"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(t(lang, "freq_1"), callback_data="freq_1"),
                InlineKeyboardButton(t(lang, "freq_2"), callback_data="freq_2"),
            ],
            [
                InlineKeyboardButton(t(lang, "freq_3"), callback_data="freq_3"),
                InlineKeyboardButton(t(lang, "freq_4"), callback_data="freq_4"),
            ],
            [InlineKeyboardButton(t(lang, "freq_custom_btn"), callback_data="freq_custom")],
        ]),
    )
    return SETUP_FREQ


async def setup_freq_btn(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    if query.data == "freq_custom":
        await query.edit_message_text(t(lang, "freq_custom_ask"))
        return SETUP_FREQ_CUSTOM
    ctx.user_data["setup"]["freq"] = int(query.data.split("_")[1])
    await query.edit_message_text("⏳")
    return await _show_preview(query.message, ctx)


async def setup_freq_custom(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    try:
        freq = int(update.message.text.strip())
        if not (1 <= freq <= 60):
            raise ValueError
    except ValueError:
        await update.message.reply_text(t(lang, "freq_invalid"))
        return SETUP_FREQ_CUSTOM
    ctx.user_data["setup"]["freq"] = freq
    return await _show_preview(update.message, ctx)


async def _show_preview(message, ctx) -> int:
    lang     = get_lang(ctx)
    s        = ctx.user_data["setup"]
    freq     = s["freq"]
    interval = round(60 / freq, 1)
    await message.reply_text(
        t(lang, "preview", chat=s["chat_id"], freq=freq, interval=interval, text=s["text"]),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_confirm"), callback_data="setup_confirm"),
            InlineKeyboardButton(t(lang, "btn_cancel"),  callback_data="setup_cancel"),
        ]]),
    )
    return SETUP_CONFIRM


async def setup_confirm(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    s    = ctx.user_data.get("setup", {})
    bd   = ctx.bot_data
    bd["cargo_text"]     = s["text"]
    bd["target_chat"]    = s["chat_id"]
    bd["freq"]           = s["freq"]
    bd["posting_active"] = True

    for job in ctx.job_queue.get_jobs_by_name("cargo"):
        job.schedule_removal()
    ctx.job_queue.run_repeating(_post_cargo, interval=60 / s["freq"], first=0, name="cargo")
    ctx.user_data["setup"] = {}

    await query.edit_message_text(
        f"{t(lang, 'panel_header')}\n\n{t(lang, 'started')}\n\n"
        + _settings_summary(lang, bd),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_panel_keyboard(lang, True),
    )
    return ConversationHandler.END


async def setup_cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["setup"] = {}
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(t(lang, "cancelled"))
    else:
        await update.message.reply_text(t(lang, "cancelled"))
    return ConversationHandler.END


# ── Health & run ──────────────────────────────────────────────────────────────

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
            app.job_queue.run_repeating(_post_cargo, interval=60 / freq, first=5, name="cargo")
            logger.info("Resumed posting → %s (%s/min)", bd["target_chat"], freq)
        await app.updater.start_polling(drop_pending_updates=True)
        await asyncio.Event().wait()


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN not set")

    persistence = PicklePersistence(filepath="bot_data.pkl")
    app = Application.builder().token(BOT_TOKEN).persistence(persistence).build()

    start_conv = ConversationHandler(
        entry_points=[CommandHandler("start", cmd_start)],
        states={
            LANG_PICK: [CallbackQueryHandler(lang_picked, pattern="^setlang_")],
        },
        fallbacks=[CommandHandler("start", cmd_start)],
        per_message=False,
    )

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

    app.add_handler(start_conv)
    app.add_handler(CommandHandler("chatid", cmd_chatid))
    app.add_handler(setup_conv)
    app.add_handler(CallbackQueryHandler(panel_btn, pattern="^panel_"))

    logger.info("Cargo bot started")
    asyncio.run(_run(app))


if __name__ == "__main__":
    main()
