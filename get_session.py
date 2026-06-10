"""
Run this ONCE locally to get your Telegram session string.
Then add the result to .env and Render as TG_SESSION.
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id   = int(input("API ID: "))
api_hash = input("API Hash: ").strip()

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n✅ Session string (add to .env as TG_SESSION):\n")
    print(client.session.save())
    print()
