import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "bot.db")


def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with _conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id   INTEGER PRIMARY KEY,
                username  TEXT,
                lang      TEXT DEFAULT 'ru',
                created_at TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER,
                username    TEXT,
                name        TEXT,
                phone       TEXT,
                dtype       TEXT,
                budget      TEXT,
                description TEXT,
                status      TEXT DEFAULT 'pending',
                created_at  TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS consultations (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id    INTEGER,
                username   TEXT,
                first_name TEXT,
                phone      TEXT,
                day        TEXT,
                time       TEXT,
                created_at TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                category    TEXT NOT NULL,
                title       TEXT NOT NULL,
                description TEXT DEFAULT '',
                file_id     TEXT DEFAULT '',
                video_url   TEXT DEFAULT '',
                demo_url    TEXT DEFAULT '',
                created_at  TEXT
            )
        """)
        conn.commit()


def upsert_user(user_id: int, username: str, lang: str):
    with _conn() as conn:
        conn.execute("""
            INSERT INTO users (user_id, username, lang, created_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                username = excluded.username,
                lang     = excluded.lang
        """, (user_id, username or "", lang, datetime.now().isoformat()))
        conn.commit()


def save_order(user_id, username, name, phone, dtype, budget, description) -> int:
    with _conn() as conn:
        cur = conn.execute("""
            INSERT INTO orders
                (user_id, username, name, phone, dtype, budget, description, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'pending', ?)
        """, (user_id, username or "", name, phone, dtype, budget, description,
              datetime.now().isoformat()))
        conn.commit()
        return cur.lastrowid


def get_order(order_id: int):
    with _conn() as conn:
        return conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()


def set_order_status(order_id: int, status: str):
    with _conn() as conn:
        conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
        conn.commit()


def all_user_ids() -> list[int]:
    with _conn() as conn:
        rows = conn.execute("SELECT user_id FROM users").fetchall()
        return [r["user_id"] for r in rows]


def pending_orders():
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM orders WHERE status = 'pending' ORDER BY created_at DESC"
        ).fetchall()


def user_count() -> int:
    with _conn() as conn:
        return conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]


def get_user_orders(user_id: int):
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,)
        ).fetchall()


def save_consultation(user_id, username, first_name, phone, day, time) -> int:
    with _conn() as conn:
        cur = conn.execute("""
            INSERT INTO consultations
                (user_id, username, first_name, phone, day, time, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, username or "", first_name or "", phone, day, time,
              datetime.now().isoformat()))
        conn.commit()
        return cur.lastrowid


def all_consultations():
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM consultations ORDER BY created_at DESC"
        ).fetchall()


# ── Portfolio ─────────────────────────────────────────────────────────────────

def add_portfolio_item(category, title, description, file_id, video_url, demo_url) -> int:
    with _conn() as conn:
        cur = conn.execute("""
            INSERT INTO portfolio
                (category, title, description, file_id, video_url, demo_url, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (category, title, description or "", file_id or "",
              video_url or "", demo_url or "", datetime.now().isoformat()))
        conn.commit()
        return cur.lastrowid


def get_portfolio_by_category(category: str):
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM portfolio WHERE category = ? ORDER BY created_at DESC",
            (category,)
        ).fetchall()


def get_portfolio_item(item_id: int):
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM portfolio WHERE id = ?", (item_id,)
        ).fetchone()


def get_all_portfolio():
    with _conn() as conn:
        return conn.execute(
            "SELECT * FROM portfolio ORDER BY category, created_at DESC"
        ).fetchall()


def delete_portfolio_item(item_id: int):
    with _conn() as conn:
        conn.execute("DELETE FROM portfolio WHERE id = ?", (item_id,))
        conn.commit()
