import asyncio
import logging
import os
from aiohttp import web
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)
from telegram.constants import ParseMode

from config import BOT_TOKEN, ADMIN_ID, ADMIN_USERNAME, SHEETS_ENABLED, CHANNEL_URL
from texts import TEXTS
from database import (
    init_db, upsert_user, all_user_ids, user_count,
    add_portfolio_item, get_portfolio_by_category,
    get_portfolio_item, get_all_portfolio, delete_portfolio_item,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Conversation states ───────────────────────────────────────────────────────
LANG_SELECT, MAIN_MENU = range(2)
BROADCAST_WAIT, BROADCAST_CONFIRM = range(10, 12)
PORT_CAT, PORT_PHOTO, PORT_TITLE, PORT_DESC, PORT_LINK, PORT_VIDEO, PORT_CONFIRM, PORT_DEL = range(20, 28)

PORTFOLIO_CATS = {
    "type_smm":      "smm",
    "type_branding": "branding",
    "type_ads":      "ads",
}
PORTFOLIO_CAT_KEYS = {v: k for k, v in PORTFOLIO_CATS.items()}


# ── Helpers ───────────────────────────────────────────────────────────────────

def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["ru"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def get_lang(ctx: ContextTypes.DEFAULT_TYPE) -> str:
    return ctx.user_data.get("lang", "ru")


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


def _s(text) -> str:
    return str(text or "—").replace("*", "").replace("_", " ").replace("`", "").replace("[", "").replace("]", "")


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "btn_portfolio"),   callback_data="portfolio"),
            InlineKeyboardButton(t(lang, "btn_contacts"),    callback_data="contacts"),
        ],
        [
            InlineKeyboardButton(t(lang, "btn_channel"),     url=CHANNEL_URL),
            InlineKeyboardButton(t(lang, "btn_switch_lang"), callback_data="switch_lang"),
        ],
    ])


def back_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")
    ]])


# ── /start ────────────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇺🇿 O'zbek",  callback_data="lang_uz"),
    ]])
    await update.message.reply_text(TEXTS["ru"]["lang_select"], reply_markup=keyboard)
    return LANG_SELECT


async def lang_selected(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = "ru" if query.data == "lang_ru" else "uz"
    ctx.user_data["lang"] = lang
    user = query.from_user
    upsert_user(user.id, user.username, lang)
    await query.edit_message_text(
        t(lang, "welcome"), reply_markup=main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN,
    )
    return MAIN_MENU


# ── Main menu handlers ────────────────────────────────────────────────────────

async def show_main_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    await query.edit_message_text(
        t(lang, "welcome"), reply_markup=main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN,
    )
    return MAIN_MENU


async def show_contacts(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    safe_username = ADMIN_USERNAME.replace("_", "\\_")
    await query.edit_message_text(
        t(lang, "contacts_text", admin_username=safe_username),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=back_keyboard(lang),
    )
    return MAIN_MENU


# ── Portfolio ─────────────────────────────────────────────────────────────────

def _portfolio_cat_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "type_smm"),      callback_data="pcat_smm_0"),
            InlineKeyboardButton(t(lang, "type_branding"), callback_data="pcat_branding_0"),
        ],
        [
            InlineKeyboardButton(t(lang, "type_ads"),      callback_data="pcat_ads_0"),
        ],
        [InlineKeyboardButton(t(lang, "btn_main_menu"),    callback_data="main_menu")],
    ])


def _portfolio_item_keyboard(lang: str, cat: str, idx: int, total: int) -> InlineKeyboardMarkup:
    nav_row = []
    if idx > 0:
        nav_row.append(InlineKeyboardButton(t(lang, "btn_port_prev"), callback_data=f"pcat_{cat}_{idx-1}"))
    nav_row.append(InlineKeyboardButton(t(lang, "portfolio_nav_btn", cur=idx+1, total=total), callback_data="noop"))
    if idx < total - 1:
        nav_row.append(InlineKeyboardButton(t(lang, "btn_port_next"), callback_data=f"pcat_{cat}_{idx+1}"))
    return InlineKeyboardMarkup([
        nav_row,
        [
            InlineKeyboardButton(t(lang, "btn_port_cats"), callback_data="portfolio"),
            InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu"),
        ],
    ])


async def show_portfolio(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    await query.edit_message_text(
        t(lang, "portfolio_select_cat"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_portfolio_cat_keyboard(lang),
    )
    return MAIN_MENU


async def show_portfolio_items(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)

    parts = query.data.split("_")
    cat   = parts[1]
    idx   = int(parts[2])

    items = get_portfolio_by_category(cat)
    nav = InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_port_cats"), callback_data="portfolio"),
        InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu"),
    ]])

    if not items:
        await query.edit_message_text(t(lang, "portfolio_empty_cat"), reply_markup=nav)
        return MAIN_MENU

    idx   = max(0, min(idx, len(items) - 1))
    item  = items[idx]
    total = len(items)

    caption = t(lang, "portfolio_item", title=item["title"], desc=item["description"] or "")
    if item["demo_url"]:
        caption += t(lang, "portfolio_demo", url=item["demo_url"])
    if item["video_url"]:
        caption += t(lang, "portfolio_video", url=item["video_url"])

    keyboard = _portfolio_item_keyboard(lang, cat, idx, total)

    try:
        if item["file_id"]:
            await query.message.delete()
            await ctx.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=item["file_id"],
                caption=caption,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=keyboard,
            )
        else:
            await query.edit_message_text(
                caption, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard
            )
    except Exception:
        await ctx.bot.send_message(
            chat_id=query.message.chat_id,
            text=caption,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=keyboard,
        )
    return MAIN_MENU


# ── Admin: portfolio management ───────────────────────────────────────────────

async def adm_port_add_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    lang = get_lang(ctx)
    ctx.user_data["new_port"] = {}
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "type_smm"),      callback_data="apc_smm"),
            InlineKeyboardButton(t(lang, "type_branding"), callback_data="apc_branding"),
        ],
        [
            InlineKeyboardButton(t(lang, "type_ads"),      callback_data="apc_ads"),
        ],
    ])
    await update.message.reply_text(
        t(lang, "adm_port_step_cat"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return PORT_CAT


async def adm_port_got_cat(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["category"] = query.data[4:]
    await query.edit_message_text(
        t(lang, "adm_port_step_photo"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_photo")
        ]]),
    )
    return PORT_PHOTO


async def adm_port_got_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    if update.message.photo:
        ctx.user_data["new_port"]["file_id"] = update.message.photo[-1].file_id
    else:
        ctx.user_data["new_port"]["file_id"] = ""
    await update.message.reply_text(t(lang, "adm_port_step_title"), parse_mode=ParseMode.MARKDOWN)
    return PORT_TITLE


async def adm_port_skip_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["file_id"] = ""
    await query.edit_message_text(t(lang, "adm_port_step_title"), parse_mode=ParseMode.MARKDOWN)
    return PORT_TITLE


async def adm_port_got_title(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["title"] = update.message.text.strip()
    await update.message.reply_text(
        t(lang, "adm_port_step_desc"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_desc")
        ]]),
    )
    return PORT_DESC


async def adm_port_got_desc(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["description"] = update.message.text.strip()
    await update.message.reply_text(
        t(lang, "adm_port_step_link"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_link")
        ]]),
    )
    return PORT_LINK


async def adm_port_skip_field(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    field = query.data.split("_")[2]
    ctx.user_data["new_port"][field] = ""

    if field == "desc":
        ctx.user_data["new_port"]["description"] = ""
        await query.edit_message_text(
            t(lang, "adm_port_step_link"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_link")
            ]]),
        )
        return PORT_LINK
    elif field == "link":
        ctx.user_data["new_port"]["demo_url"] = ""
        await query.edit_message_text(
            t(lang, "adm_port_step_video"),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_video")
            ]]),
        )
        return PORT_VIDEO
    else:
        ctx.user_data["new_port"]["video_url"] = ""
        return await _adm_port_show_preview(query, ctx, lang)


async def adm_port_got_link(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["demo_url"] = update.message.text.strip()
    await update.message.reply_text(
        t(lang, "adm_port_step_video"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_skip"), callback_data="port_skip_video")
        ]]),
    )
    return PORT_VIDEO


async def adm_port_got_video(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["new_port"]["video_url"] = update.message.text.strip()
    await update.message.reply_text("⏳")
    await update.message.get_bot().send_message(
        chat_id=update.effective_chat.id,
        text=_port_preview_text(ctx, lang),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_port_confirm_keyboard(lang),
    )
    return PORT_CONFIRM


async def _adm_port_show_preview(query, ctx, lang: str) -> int:
    await query.edit_message_text(
        _port_preview_text(ctx, lang),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_port_confirm_keyboard(lang),
    )
    return PORT_CONFIRM


def _port_preview_text(ctx, lang: str) -> str:
    p = ctx.user_data.get("new_port", {})
    cat_label = t(lang, PORTFOLIO_CAT_KEYS.get(p.get("category", ""), "type_smm"))
    return t(lang, "adm_port_preview",
        cat=cat_label,
        title=p.get("title", "—"),
        desc=p.get("description") or "—",
        demo=p.get("demo_url") or "—",
        video=p.get("video_url") or "—",
        photo="✅ Bor" if p.get("file_id") else "❌ Yo'q",
    )


def _port_confirm_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_save"),   callback_data="port_save"),
        InlineKeyboardButton(t(lang, "btn_del_no"), callback_data="port_cancel"),
    ]])


async def adm_port_save(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    p = ctx.user_data.get("new_port", {})
    add_portfolio_item(
        category=p.get("category", "smm"),
        title=p.get("title", ""),
        description=p.get("description", ""),
        file_id=p.get("file_id", ""),
        video_url=p.get("video_url", ""),
        demo_url=p.get("demo_url", ""),
    )
    ctx.user_data["new_port"] = {}
    await query.edit_message_text(t(lang, "adm_port_saved"))
    return ConversationHandler.END


async def adm_port_cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["new_port"] = {}
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(t(lang, "adm_port_cancelled"))
    else:
        await update.message.reply_text(t(lang, "adm_port_cancelled"))
    return ConversationHandler.END


async def adm_port_delete_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    lang = get_lang(ctx)
    items = get_all_portfolio()
    if not items:
        await update.message.reply_text(t(lang, "adm_port_empty"))
        return ConversationHandler.END

    lines = [t(lang, "adm_port_list_title")]
    for item in items:
        cat_label = t(lang, PORTFOLIO_CAT_KEYS.get(item["category"], "type_smm"))
        lines.append(t(lang, "adm_port_list_row",
            id=item["id"], cat=cat_label, title=item["title"]))

    buttons = []
    for item in items:
        buttons.append([InlineKeyboardButton(
            f"🗑 #{item['id']} — {item['title'][:30]}",
            callback_data=f"pdel_{item['id']}",
        )])
    buttons.append([InlineKeyboardButton("❌ Yopish", callback_data="pdel_cancel")])

    await update.message.reply_text(
        "".join(lines),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    return PORT_DEL


async def adm_port_del_pick(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)

    if query.data == "pdel_cancel":
        await query.edit_message_reply_markup(reply_markup=None)
        return ConversationHandler.END

    item_id = int(query.data.split("_")[1])
    item = get_portfolio_item(item_id)
    if not item:
        await query.edit_message_text("❌ Topilmadi.")
        return ConversationHandler.END

    await query.edit_message_text(
        t(lang, "adm_port_del_confirm", id=item["id"], title=item["title"]),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_del_yes"), callback_data=f"pdelconfirm_{item_id}"),
            InlineKeyboardButton(t(lang, "btn_del_no"),  callback_data="pdel_cancel"),
        ]]),
    )
    return PORT_DEL


async def adm_port_del_confirm(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)

    if query.data == "pdel_cancel":
        await query.edit_message_reply_markup(reply_markup=None)
        return ConversationHandler.END

    item_id = int(query.data.split("_")[1])
    delete_portfolio_item(item_id)
    await query.edit_message_text(t(lang, "adm_port_deleted", id=item_id))
    return ConversationHandler.END


# ── Language switch ───────────────────────────────────────────────────────────

async def switch_lang(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = "uz" if get_lang(ctx) == "ru" else "ru"
    ctx.user_data["lang"] = lang
    upsert_user(query.from_user.id, query.from_user.username, lang)
    await query.edit_message_text(
        t(lang, "welcome"), reply_markup=main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN,
    )
    return MAIN_MENU


# ── Admin: /broadcast ─────────────────────────────────────────────────────────

async def broadcast_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    count = user_count()
    await update.message.reply_text(
        f"📢 *Xabar yuborish*\n\nFoydalanuvchilar: *{count}*\n\nXabar matnini yozing:",
        parse_mode=ParseMode.MARKDOWN,
    )
    return BROADCAST_WAIT


async def broadcast_got_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["broadcast_text"] = update.message.text
    count = user_count()
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Yuborish", callback_data="bc_yes"),
        InlineKeyboardButton("❌ Bekor",   callback_data="bc_no"),
    ]])
    await update.message.reply_text(
        f"📢 *{count}* foydalanuvchiga xabar:\n\n———\n{update.message.text}\n———\n\nTasdiqlaysizmi?",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return BROADCAST_CONFIRM


async def broadcast_yes(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text     = ctx.user_data.get("broadcast_text", "")
    user_ids = all_user_ids()
    await query.edit_message_text(f"📤 {len(user_ids)} foydalanuvchiga yuborilmoqda...")
    sent = failed = 0
    for uid in user_ids:
        try:
            await ctx.bot.send_message(chat_id=uid, text=text)
            sent += 1
        except Exception:
            failed += 1
    await query.message.reply_text(f"✅ Tayyor. Yuborildi: {sent} | Xato: {failed}")
    return ConversationHandler.END


async def broadcast_no(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("❌ Xabar yuborish bekor qilindi.")
    return ConversationHandler.END


# ── Fallback ──────────────────────────────────────────────────────────────────

async def unknown_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(ctx)
    await update.message.reply_text(t(lang, "welcome"), reply_markup=main_menu_keyboard(lang),
                                    parse_mode=ParseMode.MARKDOWN)


# ── App setup ─────────────────────────────────────────────────────────────────

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set in .env")
    if not ADMIN_ID:
        raise RuntimeError("ADMIN_ID is not set in .env")

    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    broadcast_conv = ConversationHandler(
        entry_points=[CommandHandler("broadcast", broadcast_start)],
        states={
            BROADCAST_WAIT:    [MessageHandler(filters.TEXT & ~filters.COMMAND, broadcast_got_message)],
            BROADCAST_CONFIRM: [
                CallbackQueryHandler(broadcast_yes, pattern="^bc_yes$"),
                CallbackQueryHandler(broadcast_no,  pattern="^bc_no$"),
            ],
        },
        fallbacks=[CommandHandler("cancel", broadcast_no)],
        per_message=False,
    )

    user_conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANG_SELECT: [
                CallbackQueryHandler(lang_selected, pattern="^lang_(ru|uz)$"),
            ],
            MAIN_MENU: [
                CallbackQueryHandler(show_main_menu,       pattern="^main_menu$"),
                CallbackQueryHandler(show_portfolio,       pattern="^portfolio$"),
                CallbackQueryHandler(show_portfolio_items, pattern="^pcat_"),
                CallbackQueryHandler(show_contacts,        pattern="^contacts$"),
                CallbackQueryHandler(switch_lang,          pattern="^switch_lang$"),
                CallbackQueryHandler(lambda u, c: u.callback_query.answer(), pattern="^noop$"),
            ],
        },
        fallbacks=[
            CommandHandler("start", start),
            MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message),
        ],
        per_message=False,
        allow_reentry=True,
    )

    add_port_conv = ConversationHandler(
        entry_points=[CommandHandler("addportfolio", adm_port_add_start)],
        states={
            PORT_CAT:     [CallbackQueryHandler(adm_port_got_cat,    pattern="^apc_")],
            PORT_PHOTO:   [
                MessageHandler(filters.PHOTO, adm_port_got_photo),
                CallbackQueryHandler(adm_port_skip_photo, pattern="^port_skip_photo$"),
            ],
            PORT_TITLE:   [MessageHandler(filters.TEXT & ~filters.COMMAND, adm_port_got_title)],
            PORT_DESC:    [
                MessageHandler(filters.TEXT & ~filters.COMMAND, adm_port_got_desc),
                CallbackQueryHandler(adm_port_skip_field, pattern="^port_skip_desc$"),
            ],
            PORT_LINK:    [
                MessageHandler(filters.TEXT & ~filters.COMMAND, adm_port_got_link),
                CallbackQueryHandler(adm_port_skip_field, pattern="^port_skip_link$"),
            ],
            PORT_VIDEO:   [
                MessageHandler(filters.TEXT & ~filters.COMMAND, adm_port_got_video),
                CallbackQueryHandler(adm_port_skip_field, pattern="^port_skip_video$"),
            ],
            PORT_CONFIRM: [
                CallbackQueryHandler(adm_port_save,   pattern="^port_save$"),
                CallbackQueryHandler(adm_port_cancel, pattern="^port_cancel$"),
            ],
        },
        fallbacks=[CommandHandler("cancel", adm_port_cancel)],
        per_message=False,
    )

    del_port_conv = ConversationHandler(
        entry_points=[CommandHandler("deleteportfolio", adm_port_delete_start)],
        states={
            PORT_DEL: [
                CallbackQueryHandler(adm_port_del_confirm, pattern="^pdelconfirm_"),
                CallbackQueryHandler(adm_port_del_pick,    pattern="^pdel_"),
            ],
        },
        fallbacks=[CommandHandler("cancel", adm_port_cancel)],
        per_message=False,
    )

    app.add_handler(broadcast_conv)
    app.add_handler(add_port_conv)
    app.add_handler(del_port_conv)
    app.add_handler(user_conv)

    logger.info("Markenti bot started.")
    asyncio.run(_run(app))


async def _health(request):
    return web.Response(text="OK")


async def _run(app: Application) -> None:
    port = int(os.getenv("PORT", 8080))
    web_app = web.Application()
    web_app.router.add_get("/", _health)
    runner = web.AppRunner(web_app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
    logger.info("Health check running on port %s", port)

    async with app:
        await app.start()
        await app.updater.start_polling(drop_pending_updates=True)
        await asyncio.Event().wait()


if __name__ == "__main__":
    main()
