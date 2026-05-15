import os
import psycopg2
import psycopg2.extras
from datetime import datetime

DATABASE_URL: str = os.getenv("DATABASE_URL", "")


def _conn():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    return conn


def init_db():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id    BIGINT PRIMARY KEY,
                    username   TEXT,
                    lang       TEXT DEFAULT 'ru',
                    created_at TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id          SERIAL PRIMARY KEY,
                    user_id     BIGINT,
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
            cur.execute("""
                CREATE TABLE IF NOT EXISTS consultations (
                    id         SERIAL PRIMARY KEY,
                    user_id    BIGINT,
                    username   TEXT,
                    first_name TEXT,
                    phone      TEXT,
                    day        TEXT,
                    time       TEXT,
                    created_at TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS portfolio (
                    id          SERIAL PRIMARY KEY,
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
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (user_id, username, lang, created_at)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET
                    username = EXCLUDED.username,
                    lang     = EXCLUDED.lang
            """, (user_id, username or "", lang, datetime.now().isoformat()))
        conn.commit()


def save_order(user_id, username, name, phone, dtype, budget, description) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO orders
                    (user_id, username, name, phone, dtype, budget, description, status, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, 'pending', %s)
                RETURNING id
            """, (user_id, username or "", name, phone, dtype, budget, description,
                  datetime.now().isoformat()))
            row = cur.fetchone()
        conn.commit()
        return row["id"]


def get_order(order_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
            return cur.fetchone()


def set_order_status(order_id: int, status: str):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE orders SET status = %s WHERE id = %s", (status, order_id))
        conn.commit()


def all_user_ids() -> list:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id FROM users")
            return [r["user_id"] for r in cur.fetchall()]


def pending_orders():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM orders WHERE status = 'pending' ORDER BY created_at DESC"
            )
            return cur.fetchall()


def user_count() -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS c FROM users")
            return cur.fetchone()["c"]


def get_user_orders(user_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM orders WHERE user_id = %s ORDER BY created_at DESC",
                (user_id,)
            )
            return cur.fetchall()


def get_booked_times(date_str: str) -> list:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT time FROM consultations WHERE day = %s", (date_str,)
            )
            return [r["time"] for r in cur.fetchall()]


def save_consultation(user_id, username, first_name, phone, day, time) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO consultations
                    (user_id, username, first_name, phone, day, time, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (user_id, username or "", first_name or "", phone, day, time,
                  datetime.now().isoformat()))
            row = cur.fetchone()
        conn.commit()
        return row["id"]


def all_consultations():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM consultations ORDER BY created_at DESC")
            return cur.fetchall()


# ── Portfolio ─────────────────────────────────────────────────────────────────

def add_portfolio_item(category, title, description, file_id, video_url, demo_url) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO portfolio
                    (category, title, description, file_id, video_url, demo_url, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (category, title, description or "", file_id or "",
                  video_url or "", demo_url or "", datetime.now().isoformat()))
            row = cur.fetchone()
        conn.commit()
        return row["id"]


def get_portfolio_by_category(category: str):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM portfolio WHERE category = %s ORDER BY created_at DESC",
                (category,)
            )
            return cur.fetchall()


def get_portfolio_item(item_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM portfolio WHERE id = %s", (item_id,))
            return cur.fetchone()


def get_all_portfolio():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM portfolio ORDER BY category, created_at DESC")
            return cur.fetchall()


def delete_portfolio_item(item_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM portfolio WHERE id = %s", (item_id,))
        conn.commit()
