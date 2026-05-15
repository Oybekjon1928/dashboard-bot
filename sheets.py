import logging
from datetime import datetime

logger = logging.getLogger(__name__)

_worksheet = None


def _get_ws():
    global _worksheet
    if _worksheet is not None:
        return _worksheet

    import gspread
    from config import SHEETS_CREDS_FILE, SHEETS_ID

    gc = gspread.service_account(filename=SHEETS_CREDS_FILE)
    sh = gc.open_by_key(SHEETS_ID)
    ws = sh.sheet1

    # Write header if sheet is empty
    if not ws.get_all_values():
        ws.append_row([
            "ID", "Date", "Name", "Phone", "Type",
            "Budget/Deadline", "Description", "Status",
            "Telegram ID", "Username",
        ])
    _worksheet = ws
    return ws


def log_order(order_id, name, phone, dtype, budget, description, user_id, username):
    try:
        ws = _get_ws()
        ws.append_row([
            order_id,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            name, phone, dtype, budget, description,
            "pending",
            str(user_id),
            username or "",
        ])
    except Exception as e:
        logger.warning("Google Sheets logging failed: %s", e)


def update_order_row(order_id: int, status: str):
    try:
        ws = _get_ws()
        cell = ws.find(str(order_id), in_column=1)
        if cell:
            ws.update_cell(cell.row, 8, status)
    except Exception as e:
        logger.warning("Google Sheets status update failed: %s", e)
