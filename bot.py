import asyncio
import logging
import os
from aiohttp import web
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
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

from config import BOT_TOKEN, ADMIN_ID, ADMIN_USERNAME, PORTFOLIO_DIR, SHEETS_ENABLED, CHANNEL_URL
from texts import TEXTS
from database import (
    init_db, upsert_user, save_order, get_order,
    set_order_status, all_user_ids, pending_orders, user_count,
    get_user_orders, save_consultation, all_consultations,
    add_portfolio_item, get_portfolio_by_category,
    get_portfolio_item, get_all_portfolio, delete_portfolio_item,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

if SHEETS_ENABLED:
    import sheets as gsheets
    logger.info("Google Sheets logging enabled")

# ── Conversation states ───────────────────────────────────────────────────────
(
    LANG_SELECT,
    MAIN_MENU,
    ORDER_NAME,
    ORDER_PHONE,
    ORDER_TYPE,
    ORDER_BUDGET,
    ORDER_DESC,
    ORDER_CONFIRM,
    CALC_SOURCES,
    CALC_DEADLINE,
) = range(10)

BROADCAST_WAIT, BROADCAST_CONFIRM = range(10, 12)
CONSULT_TIME, CONSULT_PHONE = range(12, 14)
PORT_CAT, PORT_PHOTO, PORT_TITLE, PORT_DESC, PORT_LINK, PORT_VIDEO, PORT_CONFIRM, PORT_DEL = range(20, 28)

# ── Pricing tables ────────────────────────────────────────────────────────────
_BASE = {
    "type_excel":     (10, 30),
    "type_analytics": (20, 50),
    "type_bi":        (30, 80),
    "type_web":       (50, 150),
}
_SRC_MULT = {
    "calc_src_1_2": 1.0,
    "calc_src_3_5": 1.3,
    "calc_src_6":   1.7,
}
_DL_MULT = {
    "calc_dl_urgent": 1.5,
    "calc_dl_normal": 1.0,
    "calc_dl_flex":   0.9,
}

FAQ_COUNT = 5


def _price(type_key: str, src_key: str, dl_key: str) -> tuple[int, int]:
    lo, hi = _BASE.get(type_key, (100, 200))
    sm = _SRC_MULT.get(src_key, 1.0)
    dm = _DL_MULT.get(dl_key, 1.0)
    return round(lo * sm * dm), round(hi * sm * dm)


# ── Helpers ───────────────────────────────────────────────────────────────────

def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["ru"]).get(key, key)
    return text.format(**kwargs) if kwargs else text


def get_lang(ctx: ContextTypes.DEFAULT_TYPE) -> str:
    return ctx.user_data.get("lang", "ru")


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "btn_services"),    callback_data="services"),
            InlineKeyboardButton(t(lang, "btn_faq"),         callback_data="faq"),
        ],
        [InlineKeyboardButton(t(lang, "btn_portfolio"),      callback_data="portfolio")],
        [InlineKeyboardButton(t(lang, "btn_calc"),           callback_data="calc")],
        [InlineKeyboardButton(t(lang, "btn_consult"),        callback_data="consult")],
        [InlineKeyboardButton(t(lang, "btn_order"),          callback_data="order")],
        [InlineKeyboardButton(t(lang, "btn_myorders"),       callback_data="myorders")],
        [InlineKeyboardButton(t(lang, "btn_channel"),        url=CHANNEL_URL)],
        [
            InlineKeyboardButton(t(lang, "btn_contacts"),    callback_data="contacts"),
            InlineKeyboardButton(t(lang, "btn_switch_lang"), callback_data="switch_lang"),
        ],
    ])


def back_to_menu_keyboard(lang: str, include_order: bool = True) -> InlineKeyboardMarkup:
    rows = []
    if include_order:
        rows.append([InlineKeyboardButton(t(lang, "btn_order"), callback_data="order")])
    rows.append([InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")])
    return InlineKeyboardMarkup(rows)


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
        t(lang, "welcome"), reply_markup=main_menu_keyboard(lang)
    )
    return MAIN_MENU


# ── Main menu handlers ────────────────────────────────────────────────────────

async def show_main_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    await query.edit_message_text(t(lang, "welcome"), reply_markup=main_menu_keyboard(lang))
    return MAIN_MENU


async def show_services(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    await query.edit_message_text(
        t(lang, "services_text"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=back_to_menu_keyboard(lang),
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
        reply_markup=back_to_menu_keyboard(lang),
    )
    return MAIN_MENU


PORTFOLIO_CATS = {
    "type_excel":     "excel",
    "type_bi":        "bi",
    "type_web":       "web",
    "type_analytics": "analytics",
}
PORTFOLIO_CAT_KEYS = {v: k for k, v in PORTFOLIO_CATS.items()}


def _portfolio_cat_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "type_excel"),     callback_data="pcat_excel_0"),
            InlineKeyboardButton(t(lang, "type_bi"),        callback_data="pcat_bi_0"),
        ],
        [
            InlineKeyboardButton(t(lang, "type_web"),       callback_data="pcat_web_0"),
            InlineKeyboardButton(t(lang, "type_analytics"), callback_data="pcat_analytics_0"),
        ],
        [InlineKeyboardButton(t(lang, "btn_main_menu"),     callback_data="main_menu")],
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
        [InlineKeyboardButton(t(lang, "btn_port_order"),  callback_data="order")],
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

    # callback_data: "pcat_excel_2"
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
            InlineKeyboardButton(t(lang, "type_excel"),     callback_data="apc_excel"),
            InlineKeyboardButton(t(lang, "type_bi"),        callback_data="apc_bi"),
        ],
        [
            InlineKeyboardButton(t(lang, "type_web"),       callback_data="apc_web"),
            InlineKeyboardButton(t(lang, "type_analytics"), callback_data="apc_analytics"),
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
    ctx.user_data["new_port"]["category"] = query.data[4:]  # "apc_excel" → "excel"
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
    field = query.data.split("_")[2]  # "port_skip_desc" → "desc"
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
    msg = await update.message.get_bot().send_message(
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
    cat_label = t(lang, PORTFOLIO_CAT_KEYS.get(p.get("category", ""), "type_excel"))
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
        InlineKeyboardButton(t(lang, "btn_save"),    callback_data="port_save"),
        InlineKeyboardButton(t(lang, "btn_del_no"),  callback_data="port_cancel"),
    ]])


async def adm_port_save(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    p = ctx.user_data.get("new_port", {})
    add_portfolio_item(
        category=p.get("category", "excel"),
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
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["new_port"] = {}
    await query.edit_message_text(t(lang, "adm_port_cancelled"))
    return ConversationHandler.END


# Delete portfolio
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
        cat_label = t(lang, PORTFOLIO_CAT_KEYS.get(item["category"], "type_excel"))
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


# ── Language switch ──────────────────────────────────────────────────────────

async def switch_lang(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = "uz" if get_lang(ctx) == "ru" else "ru"
    ctx.user_data["lang"] = lang
    upsert_user(query.from_user.id, query.from_user.username, lang)
    await query.edit_message_text(t(lang, "welcome"), reply_markup=main_menu_keyboard(lang))
    return MAIN_MENU


# ── My orders ─────────────────────────────────────────────────────────────────

async def _myorders_text(lang: str, user_id: int) -> tuple[str, InlineKeyboardMarkup]:
    orders = get_user_orders(user_id)
    nav = InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_order"),     callback_data="order"),
        InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu"),
    ]])
    if not orders:
        return t(lang, "myorders_empty"), nav
    status_map = {
        "pending":  t(lang, "status_pending"),
        "done":     t(lang, "status_done"),
        "rejected": t(lang, "status_rejected"),
    }
    lines = [t(lang, "myorders_header")]
    for o in orders:
        lines.append(t(lang, "myorders_row",
            status=status_map.get(o["status"], "⏳"),
            id=o["id"],
            dtype=o["dtype"],
            budget=o["budget"],
            date=o["created_at"][:10],
        ))
    return "\n".join(lines), nav


async def my_orders(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(ctx)
    text, nav = await _myorders_text(lang, update.effective_user.id)
    await update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=nav)


async def my_orders_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    text, nav = await _myorders_text(lang, query.from_user.id)
    await query.edit_message_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=nav)
    return MAIN_MENU


# ── Reminder ──────────────────────────────────────────────────────────────────

def _cancel_reminder(ctx: ContextTypes.DEFAULT_TYPE, user_id: int) -> None:
    for job in ctx.job_queue.get_jobs_by_name(f"reminder_{user_id}"):
        job.schedule_removal()


async def _send_reminder(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = ctx.job.data["user_id"]
    lang    = ctx.job.data["lang"]
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(t(lang, "btn_reminder_continue"), callback_data="reminder_continue"),
        InlineKeyboardButton(t(lang, "btn_reminder_cancel"),   callback_data="reminder_cancel"),
    ]])
    try:
        await ctx.bot.send_message(
            chat_id=user_id,
            text=t(lang, "reminder_text"),
            reply_markup=keyboard,
        )
    except Exception as e:
        logger.warning("Could not send reminder to %s: %s", user_id, e)


async def reminder_continue(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_reply_markup(reply_markup=None)


async def reminder_cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["order"] = {}
    _cancel_reminder(ctx, query.from_user.id)
    await query.edit_message_text(
        t(lang, "reminder_cancelled"),
        reply_markup=main_menu_keyboard(lang),
    )
    return MAIN_MENU


# ── Free consultation ─────────────────────────────────────────────────────────

async def consult_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["consult"] = {}
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "consult_day_0"), callback_data="cday_0"),
            InlineKeyboardButton(t(lang, "consult_day_1"), callback_data="cday_1"),
            InlineKeyboardButton(t(lang, "consult_day_2"), callback_data="cday_2"),
        ],
        [InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, "consult_step1"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return CONSULT_TIME


async def consult_got_day(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    day_index = int(query.data.split("_")[1])
    ctx.user_data["consult"]["day"] = t(lang, f"consult_day_{day_index}")
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "consult_t_9"),  callback_data="ctime_9"),
            InlineKeyboardButton(t(lang, "consult_t_11"), callback_data="ctime_11"),
            InlineKeyboardButton(t(lang, "consult_t_13"), callback_data="ctime_13"),
        ],
        [
            InlineKeyboardButton(t(lang, "consult_t_15"), callback_data="ctime_15"),
            InlineKeyboardButton(t(lang, "consult_t_17"), callback_data="ctime_17"),
        ],
        [InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, "consult_step2"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return CONSULT_PHONE


async def consult_got_time(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    time_key = query.data.split("_")[1]
    ctx.user_data["consult"]["time"] = t(lang, f"consult_t_{time_key}")
    await query.edit_message_text(
        t(lang, "consult_step3"),
        parse_mode=ParseMode.MARKDOWN,
    )
    return CONSULT_PHONE


async def consult_got_phone(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    phone = update.message.text.strip()
    consult = ctx.user_data.get("consult", {})
    user = update.effective_user

    consult_id = save_consultation(
        user_id=user.id,
        username=user.username,
        first_name=user.first_name,
        phone=phone,
        day=consult.get("day", "—"),
        time=consult.get("time", "—"),
    )

    admin_text = t("uz", "admin_consult_notify",
        consult_id=consult_id,
        name=user.first_name or "—",
        username=user.username or "—",
        phone=phone,
        day=consult.get("day", "—"),
        time=consult.get("time", "—"),
        user_id=user.id,
    )
    try:
        await update.message.bot.send_message(
            chat_id=ADMIN_ID, text=admin_text, parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error("Consult admin notify failed: %s", e)

    # Schedule 15-min repeat reminder to admin
    ctx.job_queue.run_once(
        _remind_admin_consult,
        when=900,
        data={
            "consult_id": consult_id,
            "name": user.first_name or "—",
            "phone": phone,
            "day": consult.get("day", "—"),
            "time": consult.get("time", "—"),
        },
        name=f"con_remind_{consult_id}",
    )

    await update.message.reply_text(
        t(lang, "consult_confirm",
          day=consult.get("day", "—"),
          time=consult.get("time", "—"),
          phone=phone,
          admin_username=ADMIN_USERNAME),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")
        ]]),
    )
    ctx.user_data["consult"] = {}
    return MAIN_MENU


# ── FAQ ───────────────────────────────────────────────────────────────────────

def _faq_list_keyboard(lang: str) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(t(lang, f"faq_q{i}"), callback_data=f"faq_{i}")]
        for i in range(1, FAQ_COUNT + 1)
    ]
    rows.append([InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")])
    return InlineKeyboardMarkup(rows)


async def show_faq(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    await query.edit_message_text(
        t(lang, "faq_menu"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_faq_list_keyboard(lang),
    )
    return MAIN_MENU


async def show_faq_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    n = query.data.split("_")[1]  # "faq_3" → "3"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "btn_back_faq"), callback_data="faq")],
        [InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, f"faq_a{n}"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return MAIN_MENU


# ── Pricing calculator ────────────────────────────────────────────────────────

def _type_keyboard(prefix: str, lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(t(lang, "type_bi"),        callback_data=f"{prefix}type_bi"),
            InlineKeyboardButton(t(lang, "type_web"),       callback_data=f"{prefix}type_web"),
        ],
        [
            InlineKeyboardButton(t(lang, "type_excel"),     callback_data=f"{prefix}type_excel"),
            InlineKeyboardButton(t(lang, "type_analytics"), callback_data=f"{prefix}type_analytics"),
        ],
        [InlineKeyboardButton(t(lang, "btn_main_menu"),     callback_data="main_menu")],
    ])


async def calc_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["calc"] = {}
    await query.edit_message_text(
        t(lang, "calc_step1"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_type_keyboard("calc_", lang),
    )
    return CALC_SOURCES


async def calc_got_type(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    # callback_data is "calc_type_bi" → strip "calc_" prefix to get type key
    ctx.user_data["calc"]["type_key"] = query.data[5:]  # "type_bi"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "calc_src_1_2"), callback_data="calc_src_1_2")],
        [InlineKeyboardButton(t(lang, "calc_src_3_5"), callback_data="calc_src_3_5")],
        [InlineKeyboardButton(t(lang, "calc_src_6"),   callback_data="calc_src_6")],
        [InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, "calc_step2"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return CALC_DEADLINE


async def calc_got_sources(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["calc"]["src_key"] = query.data  # "calc_src_3_5"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "calc_dl_urgent"), callback_data="calc_dl_urgent")],
        [InlineKeyboardButton(t(lang, "calc_dl_normal"), callback_data="calc_dl_normal")],
        [InlineKeyboardButton(t(lang, "calc_dl_flex"),   callback_data="calc_dl_flex")],
        [InlineKeyboardButton(t(lang, "btn_main_menu"),  callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, "calc_step3"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return MAIN_MENU


async def calc_got_deadline(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    calc = ctx.user_data.get("calc", {})
    type_key = calc.get("type_key", "type_analytics")
    src_key  = calc.get("src_key",  "calc_src_1_2")
    dl_key   = query.data

    lo, hi = _price(type_key, src_key, dl_key)

    dtype    = t(lang, type_key)
    sources  = t(lang, src_key.replace("calc_", "calc_"))
    deadline = t(lang, dl_key.replace("calc_", "calc_"))

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "btn_calc_order"), callback_data="order")],
        [InlineKeyboardButton(t(lang, "btn_recalc"),     callback_data="calc")],
        [InlineKeyboardButton(t(lang, "btn_main_menu"),  callback_data="main_menu")],
    ])
    await query.edit_message_text(
        t(lang, "calc_result",
          dtype=dtype, sources=sources, deadline=deadline,
          min_p=lo, max_p=hi),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return MAIN_MENU


# ── Order flow ────────────────────────────────────────────────────────────────

async def order_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["order"] = {}

    # Schedule 1-hour reminder
    user_id = query.from_user.id
    _cancel_reminder(ctx, user_id)
    ctx.job_queue.run_once(
        _send_reminder,
        when=3600,
        data={"user_id": user_id, "lang": lang},
        name=f"reminder_{user_id}",
    )

    await query.edit_message_text(t(lang, "order_start"), parse_mode=ParseMode.MARKDOWN)
    return ORDER_NAME


async def order_name(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["order"]["name"] = update.message.text.strip()
    await update.message.reply_text(t(lang, "order_phone"), parse_mode=ParseMode.MARKDOWN)
    return ORDER_PHONE


async def order_phone(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["order"]["phone"] = update.message.text.strip()
    await update.message.reply_text(
        t(lang, "order_type"),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=_type_keyboard("", lang),
    )
    return ORDER_TYPE


async def order_type(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["order"]["dtype"] = t(lang, query.data)
    await query.edit_message_text(t(lang, "order_budget"), parse_mode=ParseMode.MARKDOWN)
    return ORDER_BUDGET


async def order_budget(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["order"]["budget"] = update.message.text.strip()
    await update.message.reply_text(t(lang, "order_desc"), parse_mode=ParseMode.MARKDOWN)
    return ORDER_DESC


async def order_desc(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    lang = get_lang(ctx)
    ctx.user_data["order"]["desc"] = update.message.text.strip()
    order = ctx.user_data["order"]
    await update.message.reply_text(
        t(lang, "order_confirm", **order),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_confirm"), callback_data="confirm_yes"),
            InlineKeyboardButton(t(lang, "btn_cancel"),  callback_data="confirm_no"),
        ]]),
    )
    return ORDER_CONFIRM


async def order_confirm_yes(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    order = ctx.user_data.get("order", {})
    user  = query.from_user

    order_id = save_order(
        user_id=user.id,
        username=user.username,
        name=order.get("name", ""),
        phone=order.get("phone", ""),
        dtype=order.get("dtype", ""),
        budget=order.get("budget", ""),
        description=order.get("desc", ""),
    )

    if SHEETS_ENABLED:
        gsheets.log_order(
            order_id=order_id,
            name=order.get("name", ""),
            phone=order.get("phone", ""),
            dtype=order.get("dtype", ""),
            budget=order.get("budget", ""),
            description=order.get("desc", ""),
            user_id=user.id,
            username=user.username,
        )

    admin_text = t("uz", "admin_order_notify",
        order_id=order_id,
        name=order.get("name", "—"),
        phone=order.get("phone", "—"),
        dtype=order.get("dtype", "—"),
        budget=order.get("budget", "—"),
        desc=order.get("desc", "—"),
        user_id=user.id,
        username=user.username or "—",
    )
    try:
        await ctx.bot.send_message(
            chat_id=ADMIN_ID, text=admin_text, parse_mode=ParseMode.MARKDOWN
        )
    except Exception as e:
        logger.error("Admin notification failed: %s", e)

    # Schedule 15-min repeat reminder to admin
    ctx.job_queue.run_once(
        _remind_admin_order,
        when=900,
        data={"order_id": order_id, "order": dict(order)},
        name=f"ord_remind_{order_id}",
    )

    await query.edit_message_text(
        t(lang, "order_sent", admin_username=ADMIN_USERNAME),
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(t(lang, "btn_main_menu"), callback_data="main_menu")
        ]]),
    )
    ctx.user_data["order"] = {}
    _cancel_reminder(ctx, query.from_user.id)
    return MAIN_MENU


async def order_confirm_no(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = get_lang(ctx)
    ctx.user_data["order"] = {}
    _cancel_reminder(ctx, query.from_user.id)
    await query.edit_message_text(
        t(lang, "order_cancelled"), reply_markup=main_menu_keyboard(lang)
    )
    return MAIN_MENU


# ── Admin order/consult reminder jobs ────────────────────────────────────────

async def _remind_admin_order(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    data     = ctx.job.data
    order_id = data["order_id"]
    order    = data["order"]
    text = t("uz", "admin_order_remind",
        order_id=order_id,
        name=order.get("name", "—"),
        phone=order.get("phone", "—"),
        dtype=order.get("dtype", "—"),
        budget=order.get("budget", "—"),
    )
    try:
        await ctx.bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logger.warning("Order remind failed: %s", e)


async def _remind_admin_consult(ctx: ContextTypes.DEFAULT_TYPE) -> None:
    data = ctx.job.data
    text = t("uz", "admin_consult_remind",
        consult_id=data["consult_id"],
        name=data["name"],
        phone=data["phone"],
        day=data["day"],
        time=data["time"],
    )
    try:
        await ctx.bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        logger.warning("Consult remind failed: %s", e)


async def admin_accept_order(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    if not ctx.args:
        await update.message.reply_text("Ishlatish: `/accept <order_id>`", parse_mode=ParseMode.MARKDOWN)
        return
    order_id = int(ctx.args[0])
    # Cancel reminder job
    for job in ctx.job_queue.get_jobs_by_name(f"ord_remind_{order_id}"):
        job.schedule_removal()
    order = get_order(order_id)
    if not order:
        await update.message.reply_text(t("uz", "admin_accept_404", id=order_id))
        return
    await update.message.reply_text(t("uz", "admin_accepted", id=order_id))
    # Notify user
    try:
        await ctx.bot.send_message(
            chat_id=order["user_id"],
            text=(
                f"✅ Sizning buyurtmangiz *#{order_id}* menejer tomonidan qabul qilindi\\!\n"
                f"Tez orada siz bilan bog'lanamiz\\."
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except Exception:
        pass


async def admin_accept_consult(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    if not ctx.args:
        await update.message.reply_text("Ishlatish: `/acceptc <consult_id>`", parse_mode=ParseMode.MARKDOWN)
        return
    consult_id = int(ctx.args[0])
    for job in ctx.job_queue.get_jobs_by_name(f"con_remind_{consult_id}"):
        job.schedule_removal()
    await update.message.reply_text(f"✅ Konsultatsiya #{consult_id} qabul qilindi.")


# ── Admin: /done /reject /orders ──────────────────────────────────────────────

async def admin_done(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    if not ctx.args:
        await update.message.reply_text("Использование: `/done <order_id>`", parse_mode=ParseMode.MARKDOWN)
        return
    order_id = int(ctx.args[0])
    order = get_order(order_id)
    if not order:
        await update.message.reply_text(f"Заявка #{order_id} не найдена.")
        return
    set_order_status(order_id, "done")
    if SHEETS_ENABLED:
        gsheets.update_order_row(order_id, "done")
    try:
        await ctx.bot.send_message(
            chat_id=order["user_id"],
            text=(
                f"✅ Ваш заказ *\\#{order_id}* выполнен\\! "
                f"Спасибо за доверие\\. Свяжитесь с нами: @{ADMIN_USERNAME}"
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except Exception as e:
        logger.warning("Could not notify user: %s", e)
    await update.message.reply_text(f"✅ Заявка #{order_id} выполнена.")


async def admin_reject(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    if not ctx.args:
        await update.message.reply_text("Использование: `/reject <order_id> [причина]`", parse_mode=ParseMode.MARKDOWN)
        return
    order_id = int(ctx.args[0])
    reason   = " ".join(ctx.args[1:]) if len(ctx.args) > 1 else "Не указана"
    order = get_order(order_id)
    if not order:
        await update.message.reply_text(f"Заявка #{order_id} не найдена.")
        return
    set_order_status(order_id, "rejected")
    if SHEETS_ENABLED:
        gsheets.update_order_row(order_id, "rejected")
    esc = lambda s: s.replace(".", "\\.").replace("!", "\\!").replace("-", "\\-").replace("(", "\\(").replace(")", "\\)")
    try:
        await ctx.bot.send_message(
            chat_id=order["user_id"],
            text=(
                f"❌ По заявке *\\#{order_id}* мы вынуждены отказать\\.\n"
                f"Причина: {esc(reason)}\n\n"
                f"Если есть вопросы — @{ADMIN_USERNAME}"
            ),
            parse_mode=ParseMode.MARKDOWN_V2,
        )
    except Exception as e:
        logger.warning("Could not notify user: %s", e)
    await update.message.reply_text(f"❌ Заявка #{order_id} отклонена.")


async def admin_orders(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    rows = pending_orders()
    if not rows:
        await update.message.reply_text("Faol arizalar yo'q.")
        return
    lines = [f"📋 *Faol arizalar ({len(rows)}):*\n"]
    for r in rows:
        lines.append(
            f"*#{r['id']}* — {r['name']} | {r['dtype']}\n"
            f"📱 {r['phone']} | 💰 {r['budget']}\n"
            f"🕐 {r['created_at'][:16]}\n"
        )
    await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)


async def admin_consultations(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    if not is_admin(update.effective_user.id):
        return
    rows = all_consultations()
    if not rows:
        await update.message.reply_text("📅 Hali konsultatsiya so'rovlari yo'q.")
        return
    lines = [f"📅 *Barcha konsultatsiyalar ({len(rows)}):*\n"]
    for r in rows:
        lines.append(
            f"*#{r['id']}* — {r['first_name']} (@{r['username'] or '—'})\n"
            f"📱 {r['phone']}\n"
            f"📅 {r['day']} | 🕐 {r['time']}\n"
            f"🗓 {r['created_at'][:16]}\n"
        )
    await update.message.reply_text("\n".join(lines), parse_mode=ParseMode.MARKDOWN)


# ── Admin: /broadcast ─────────────────────────────────────────────────────────

async def broadcast_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    if not is_admin(update.effective_user.id):
        return ConversationHandler.END
    count = user_count()
    await update.message.reply_text(
        f"📢 *Рассылка*\n\nПользователей в базе: *{count}*\n\nНапишите сообщение:",
        parse_mode=ParseMode.MARKDOWN,
    )
    return BROADCAST_WAIT


async def broadcast_got_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    ctx.user_data["broadcast_text"] = update.message.text
    count = user_count()
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Отправить", callback_data="bc_yes"),
        InlineKeyboardButton("❌ Отмена",    callback_data="bc_no"),
    ]])
    await update.message.reply_text(
        f"📢 Сообщение для *{count}* пользователей:\n\n———\n{update.message.text}\n———\n\nПодтвердить?",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )
    return BROADCAST_CONFIRM


async def broadcast_yes(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    text     = ctx.user_data.get("broadcast_text", "")
    user_ids = all_user_ids()
    await query.edit_message_text(f"📤 Отправляю {len(user_ids)} пользователям...")
    sent = failed = 0
    for uid in user_ids:
        try:
            await ctx.bot.send_message(chat_id=uid, text=text)
            sent += 1
        except Exception:
            failed += 1
    await query.message.reply_text(f"✅ Готово. Отправлено: {sent} | Ошибок: {failed}")
    return ConversationHandler.END


async def broadcast_no(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("❌ Рассылка отменена.")
    return ConversationHandler.END


# ── Fallback ──────────────────────────────────────────────────────────────────

async def unknown_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(ctx)
    await update.message.reply_text(t(lang, "main_menu"), reply_markup=main_menu_keyboard(lang))


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
                CallbackQueryHandler(show_main_menu,    pattern="^main_menu$"),
                CallbackQueryHandler(show_services,     pattern="^services$"),
                CallbackQueryHandler(show_portfolio,         pattern="^portfolio$"),
                CallbackQueryHandler(show_portfolio_items,   pattern="^pcat_"),
                CallbackQueryHandler(show_contacts,     pattern="^contacts$"),
                CallbackQueryHandler(show_faq,          pattern="^faq$"),
                CallbackQueryHandler(show_faq_answer,   pattern="^faq_[1-5]$"),
                CallbackQueryHandler(calc_start,        pattern="^calc$"),
                CallbackQueryHandler(order_start,       pattern="^order$"),
                CallbackQueryHandler(consult_start,       pattern="^consult$"),
                CallbackQueryHandler(switch_lang,         pattern="^switch_lang$"),
                CallbackQueryHandler(my_orders_callback,  pattern="^myorders$"),
                CallbackQueryHandler(lambda u, c: u.callback_query.answer(), pattern="^noop$"),
                CallbackQueryHandler(calc_got_deadline, pattern="^calc_dl_"),
            ],
            CALC_SOURCES: [
                CallbackQueryHandler(calc_got_type,    pattern="^calc_type_"),
                CallbackQueryHandler(show_main_menu,   pattern="^main_menu$"),
            ],
            CALC_DEADLINE: [
                CallbackQueryHandler(calc_got_sources, pattern="^calc_src_"),
                CallbackQueryHandler(show_main_menu,   pattern="^main_menu$"),
            ],
            ORDER_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, order_name),
            ],
            ORDER_PHONE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, order_phone),
            ],
            ORDER_TYPE: [
                CallbackQueryHandler(order_type,       pattern="^type_"),
                CallbackQueryHandler(show_main_menu,   pattern="^main_menu$"),
            ],
            ORDER_BUDGET: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, order_budget),
            ],
            ORDER_DESC: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, order_desc),
            ],
            ORDER_CONFIRM: [
                CallbackQueryHandler(order_confirm_yes, pattern="^confirm_yes$"),
                CallbackQueryHandler(order_confirm_no,  pattern="^confirm_no$"),
            ],
            CONSULT_TIME: [
                CallbackQueryHandler(consult_got_day,  pattern="^cday_"),
                CallbackQueryHandler(show_main_menu,   pattern="^main_menu$"),
            ],
            CONSULT_PHONE: [
                CallbackQueryHandler(consult_got_time, pattern="^ctime_"),
                MessageHandler(filters.TEXT & ~filters.COMMAND, consult_got_phone),
                CallbackQueryHandler(show_main_menu,   pattern="^main_menu$"),
            ],
        },
        fallbacks=[
            CommandHandler("start", start),
            CallbackQueryHandler(reminder_cancel, pattern="^reminder_cancel$"),
            CallbackQueryHandler(reminder_continue, pattern="^reminder_continue$"),
            MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message),
        ],
        per_message=False,
        allow_reentry=True,
    )

    app.add_handler(CommandHandler("done",          admin_done))
    app.add_handler(CommandHandler("reject",        admin_reject))
    app.add_handler(CommandHandler("orders",        admin_orders))
    app.add_handler(CommandHandler("consultations", admin_consultations))
    app.add_handler(CommandHandler("accept",        admin_accept_order))
    app.add_handler(CommandHandler("acceptc",       admin_accept_consult))
    app.add_handler(CommandHandler("myorders",      my_orders))
    # Admin: add portfolio
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

    # Admin: delete portfolio
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

    logger.info("Bot started. Sheets: %s", "enabled" if SHEETS_ENABLED else "disabled")
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
