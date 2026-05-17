import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))
ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")

PORTFOLIO_DIR = os.path.join(os.path.dirname(__file__), "portfolio")
DATABASE_URL: str = os.getenv("DATABASE_URL", "")
CHANNEL_URL: str = os.getenv("CHANNEL_URL", "https://t.me/Markentii")

SHEETS_CREDS_FILE: str = os.getenv("SHEETS_CREDS_FILE", "credentials.json")
SHEETS_ID: str = os.getenv("SHEETS_ID", "")
SHEETS_ENABLED: bool = bool(
    SHEETS_ID and os.path.exists(
        os.path.join(os.path.dirname(__file__), os.getenv("SHEETS_CREDS_FILE", "credentials.json"))
    )
)
