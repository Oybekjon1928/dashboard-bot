import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN:  str = os.getenv("BOT_TOKEN", "")
ADMIN_ID:   int = int(os.getenv("ADMIN_ID", "0"))
TG_API_ID:  int = int(os.getenv("TG_API_ID", "0"))
TG_API_HASH: str = os.getenv("TG_API_HASH", "")
TG_SESSION: str = os.getenv("TG_SESSION", "")
