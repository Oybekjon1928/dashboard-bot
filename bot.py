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
    ContextTypes,
    PicklePersistence,
    filters,
)
from telegram.constants import ParseMode
from telethon import TelegramClient
from telethon.sessions import StringSession

from config import BOT_TOKEN, ADMIN_ID, TG_API_ID, TG_API_HASH, TG_SESSION

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

tg_client: TelegramClient = None  # type: ignore

# ── Texts ─────────────────────────────────────────────────────────────────────

TEXTS = {
    "ru": {
        "not_admin":       "🚛 Cargo Bot",
        "not_configured":  "🚛 *Cargo Auto-Poster*\n\nЕщё не настроено.\nНажмите /setup чтобы настроить.",
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
        "step1":           "📝 *Шаг 1 / 3*\n\nОтправьте текст объявления:",
        "step2": (
            "📍 *Шаг 2 / 3*\n\n"
            "Укажите username или ID группы/канала.\n\n"
            "• Username: `@mygroup`\n"
            "• ID: `-1001234567890`\n\n"
            "_Вы должны быть участником этой группы_"
        ),
        "step3":           "⏱ *Шаг 3 / 3*\n\nСколько раз в минуту отправлять?",
        "freq_1":          "1 раз/мин",
        "freq_2":          "2 раза/мин",
        "freq_3":          "3 раза/мин",
        "freq_4":          "4 раза/мин",
        "freq_custom_btn": "✏️ Другое число",
        "freq_custom_ask": "✏️ Введите число раз в минуту (1–60):",
        "freq_invalid":    "❌ Введите целое число от 1 до 60.",
        "preview": (
            "👁 *Предпросмотр:*\n\n"
            "📍 Группа/канал: `{chat}`\n"
            "⏱ {freq} раз/мин (каждые {interval} сек)\n\n"
            "📝 *Сообщение:*\n{text}"
        ),
        "btn_confirm":     "✅ Запустить",
        "btn_cancel":      "❌ Отмена",
        "cancelled":       "❌ Настройка отменена.",
        "chat_invalid":    "❌ Неверный формат.\nВведите @username или числовой ID.",
        "lang_select":     "🌐 Выберите язык / Tilni tanlang:",
        "setup_done":      "✅ *Рассылка запущена!*",
    },
    "uz": {
        "not_admin":       "🚛 Yuk Boti",
        "not_configured":  "🚛 *Yuk Avto-Jo'natuvchi*\n\nHali sozlanmagan.\n/setup buyrug'ini yuboring.",
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
        "step1":           "📝 *Qadam 1 / 3*\n\nE'lon matnini yuboring:",
        "step2": (
            "📍 *Qadam 2 / 3*\n\n"
            "Guruh yoki kanal username yoki ID sini kiriting.\n\n"
            "• Username: `@mygroup`\n"
            "• ID: `-1001234567890`\n\n"
            "_Siz o'sha guruhda a'zo bo'lishingiz kerak_"
        ),
        "step3":           "⏱ *Qadam 3 / 3*\n\nDaqiqada necha marta yuborish?",
        "freq_1":          "1 marta/daq",
        "freq_2":          "2 marta/daq",
        "freq_3":          "3 marta/daq",
        "freq_4":          "4 marta/daq",
        "freq_custom_btn": "✏️ Boshqa raqam",
        "freq_custom_ask": "✏️ Daqiqada necha marta yuborishni kiriting (1–60):",
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
        "chat_invalid":    "❌ Noto'g'ri format.\n@username yoki raqamli ID kiriting.",
        "lang_select":     "🌐 Выберите язык / Tilni tanlang:",
        "setup_done":      "✅ *Yuborish boshlandi!*",
    },
}

# mode values stored in user_data:
# "idle" | "await_msg" | "await_chat" | "await_freq_custom"

def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["ru"]).get(key, key)
    return text.format(**kwargs) if kwargs else text

def get_lang(ctx: ContextTypes.DEFAULT_TYPE) -> str:
    return ctx.user_data.get("lang", "ru")

def is_admin(uid: int) -> bool:
    return uid == ADMIN_ID

def _is_running(ctx: ContextTypes.DEFAULT_TYPE) -> bool:
    return bool(ctx.job_queue.get_jobs_by_name("cargo"))

def _stop_jobs(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    for job in ctx.job_queue.get_jobs_by_name("cargo"):
        job.schedule_removal()

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

def _freq_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "freq_1"), callback_data="freq_1"),
            InlineKeyboardButton(t(lang, "freq_2"), callback_data="freq_2"),
        ],
        [
            InlineKeyboardButton(t(lang, "freq_3"), callback_data="freq_3"),
            InlineKeyboardButton(t(lang, "freq_4"), callback_data="freq_4"),
        ],
        [InlineKeyboardButton(t(lang, "freq_custom_btn"), callback_data="freq_custom")],
    ])

def _settings_summary(lang: str, bd: dict) -> str:
    chat     = bd.get("target_chat", "—")
    freq     = bd.get("freq", 1)
    interval = round(60 / freq, 1)
    text     = bd.get("cargo_text", "—")
    return (
        f"{t(lang, 'chat_label')}: `{chat}`\n"
        f"{t(lang, 'freq_label')}: {t(lang, 'freq_value', freq=freq, interval=interval)}\n\n"
        f"{t(lang, 'msg_label')}\n{text}"
    )


# ── Job ───────────────────────────────────────────────────────────────────────

async def _post_cargo(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    bd      = ctx.bot_data
    text    = bd.get("cargo_text", "")
    chat_id = bd.get("target_chat", "")
    if not text or not chat_id:
        return
    try:
        target = int(chat_id) if chat_id.lstrip("-").isdigit() else chat_id
        await tg_client.send_message(target, text)
        logger.info("Posted as user to %s", chat_id)
    except Exception as e:
        logger.error("Post failed: %s", e)


# ── /start ────────────────────────────────────────────────────────────────────

async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        await update.message.reply_text(t("ru", "not_admin"))
        return
    ctx.user_data["mode"] = "idle"
    await update.message.reply_text(
        t("ru", "lang_select"),
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("🇷🇺 Русский", callback_data="setlang_ru"),
            InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="setlang_uz"),
        ]]),
    )


async def cmd_setup(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    lang = get_lang(ctx)
    ctx.user_data["mode"]  = "await_msg"
    ctx.user_data["setup"] = {}
    await update.message.reply_text(t(lang, "step1"), parse_mode=ParseMode.MARKDOWN)


async def cmd_chatid(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Chat ID: `{update.effective_chat.id}`",
        parse_mode=ParseMode.MARKDOWN,
    )


# ── Message handler ───────────────────────────────────────────────────────────

async def on_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    lang = get_lang(ctx)
    mode = ctx.user_data.get("mode", "idle")
    text = update.message.text or ""

    if mode == "await_msg":
        ctx.user_data.setdefault("setup", {})["text"] = text
        ctx.user_data["mode"] = "await_chat"
        await update.message.reply_text(t(lang, "step2"), parse_mode=ParseMode.MARKDOWN)

    elif mode == "await_chat":
        raw = text.strip()
        if update.message.forward_from_chat:
            raw = str(update.message.forward_from_chat.id)
        if not raw.startswith("@") and not raw.lstrip("-").isdigit():
            await update.message.reply_text(t(lang, "chat_invalid"), parse_mode=ParseMode.MARKDOWN)
            return
        ctx.user_data.setdefault("setup", {})["chat_id"] = raw
        ctx.user_data["mode"] = "await_freq"
        await update.message.reply_text(
            t(lang, "step3"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_freq_keyboard(lang),
        )

    elif mode == "await_freq_custom":
        try:
            freq = int(text.strip())
            if not (1 <= freq <= 60):
                raise ValueError
        except ValueError:
            await update.message.reply_text(t(lang, "freq_invalid"))
            return
        ctx.user_data.setdefault("setup", {})["freq"] = freq
        ctx.user_data["mode"] = "await_confirm"
        await _show_preview(update.message.chat_id, ctx, lang)


# ── Callback handler ──────────────────────────────────────────────────────────

async def on_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if not is_admin(query.from_user.id):
        return

    lang = get_lang(ctx)
    data = query.data

    # ── Language selection ──
    if data.startswith("setlang_"):
        ctx.user_data["lang"]  = "uz" if data == "setlang_uz" else "ru"
        lang = ctx.user_data["lang"]
        ctx.user_data["mode"]  = "await_msg"
        ctx.user_data["setup"] = {}
        await query.edit_message_text(t(lang, "step1"), parse_mode=ParseMode.MARKDOWN)

    # ── Frequency buttons ──
    elif data.startswith("freq_") and ctx.user_data.get("mode") == "await_freq":
        if data == "freq_custom":
            ctx.user_data["mode"] = "await_freq_custom"
            await query.edit_message_text(t(lang, "freq_custom_ask"))
        else:
            freq = int(data.split("_")[1])
            ctx.user_data.setdefault("setup", {})["freq"] = freq
            ctx.user_data["mode"] = "await_confirm"
            await query.edit_message_text(t(lang, "step3"))
            await _show_preview(query.message.chat_id, ctx, lang)

    # ── Confirm / Cancel setup ──
    elif data == "setup_confirm":
        s  = ctx.user_data.get("setup", {})
        bd = ctx.bot_data
        bd["cargo_text"]     = s.get("text", "")
        bd["target_chat"]    = s.get("chat_id", "")
        bd["freq"]           = s.get("freq", 1)
        bd["posting_active"] = True
        ctx.user_data["mode"] = "idle"
        _stop_jobs(ctx)
        ctx.job_queue.run_repeating(_post_cargo, interval=60 / bd["freq"], first=0, name="cargo")
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'started')}\n\n" + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, True),
        )

    elif data == "setup_cancel":
        ctx.user_data["mode"]  = "idle"
        ctx.user_data["setup"] = {}
        await query.edit_message_text(t(lang, "cancelled"))

    # ── Panel buttons ──
    elif data == "panel_lang":
        ctx.user_data["lang"] = "uz" if lang == "ru" else "ru"
        lang = ctx.user_data["lang"]
        active = _is_running(ctx)
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'status_label')}: "
            f"{t(lang, 'running' if active else 'stopped')}\n\n"
            + _settings_summary(lang, ctx.bot_data),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, active),
        )

    elif data == "panel_setup":
        ctx.user_data["mode"]  = "await_msg"
        ctx.user_data["setup"] = {}
        await query.edit_message_text(t(lang, "step1"), parse_mode=ParseMode.MARKDOWN)

    elif data == "panel_start":
        bd = ctx.bot_data
        if not bd.get("cargo_text") or not bd.get("target_chat"):
            await query.answer(t(lang, "no_settings"), show_alert=True)
            return
        if not _is_running(ctx):
            ctx.job_queue.run_repeating(_post_cargo, interval=60 / bd.get("freq", 1), first=0, name="cargo")
        bd["posting_active"] = True
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'started')}\n\n" + _settings_summary(lang, bd),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, True),
        )

    elif data == "panel_stop":
        _stop_jobs(ctx)
        ctx.bot_data["posting_active"] = False
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'stopped_msg')}\n\n"
            + _settings_summary(lang, ctx.bot_data),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, False),
        )

    elif data == "panel_status":
        active = _is_running(ctx)
        await query.edit_message_text(
            f"{t(lang, 'panel_header')}\n\n{t(lang, 'status_label')}: "
            f"{t(lang, 'running' if active else 'stopped')}\n\n"
            + _settings_summary(lang, ctx.bot_data),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=_panel_keyboard(lang, active),
        )


async def _show_preview(chat_id: int, ctx: ContextTypes.DEFAULT_TYPE, lang: str) -> None:
    s        = ctx.user_data.get("setup", {})
    freq     = s.get("freq", 1)
    interval = round(60 / freq, 1)
    await ctx.bot.send_message(
        chat_id=chat_id,
        text=t(lang, "preview", chat=s.get("chat_id", ""), freq=freq, interval=interval, text=s.get("text", "")),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_confirm"), callback_data="setup_confirm"),
            InlineKeyboardButton(t(lang, "btn_cancel"),  callback_data="setup_cancel"),
        ]]),
    )


# ── Health & run ──────────────────────────────────────────────────────────────

async def _health(request):
    return web.Response(text="OK")


async def _run(app: Application) -> None:
    global tg_client
    tg_client = TelegramClient(StringSession(TG_SESSION), TG_API_ID, TG_API_HASH)

    port = int(os.getenv("PORT", 8080))
    web_app = web.Application()
    web_app.router.add_get("/", _health)
    runner = web.AppRunner(web_app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
    logger.info("Health server on port %s", port)

    await tg_client.start()
    logger.info("Telethon userbot connected")

    async with app:
        await app.start()
        bd = app.bot_data
        if bd.get("posting_active") and bd.get("cargo_text") and bd.get("target_chat"):
            freq = bd.get("freq", 1)
            app.job_queue.run_repeating(_post_cargo, interval=60 / freq, first=5, name="cargo")
            logger.info("Resumed posting → %s (%s/min)", bd["target_chat"], freq)
        await app.updater.start_polling(drop_pending_updates=True)
        await asyncio.Event().wait()

    await tg_client.disconnect()


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN not set")
    if not TG_API_ID or not TG_API_HASH or not TG_SESSION:
        raise RuntimeError("TG_API_ID, TG_API_HASH and TG_SESSION must all be set")

    persistence = PicklePersistence(filepath="bot_data.pkl")
    app = Application.builder().token(BOT_TOKEN).persistence(persistence).build()

    app.add_handler(CommandHandler("start",  cmd_start))
    app.add_handler(CommandHandler("setup",  cmd_setup))
    app.add_handler(CommandHandler("chatid", cmd_chatid))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))

    logger.info("Cargo userbot started")
    asyncio.run(_run(app))


if __name__ == "__main__":
    main()
