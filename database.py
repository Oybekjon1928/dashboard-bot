import os
import psycopg2
import psycopg2.extras
from datetime import datetime, timezone, timedelta

TZ_TASHKENT = timezone(timedelta(hours=5))

def now_tashkent() -> str:
    return datetime.now(TZ_TASHKENT).strftime("%Y-%m-%d %H:%M")

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
            cur.execute("""
                CREATE TABLE IF NOT EXISTS surveys (
                    id         SERIAL PRIMARY KEY,
                    title      TEXT NOT NULL,
                    is_active  BOOLEAN DEFAULT TRUE,
                    created_at TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS survey_questions (
                    id        SERIAL PRIMARY KEY,
                    survey_id INTEGER NOT NULL,
                    text      TEXT NOT NULL,
                    order_num INTEGER DEFAULT 1
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS survey_responses (
                    id         SERIAL PRIMARY KEY,
                    survey_id  INTEGER NOT NULL,
                    user_id    BIGINT,
                    username   TEXT,
                    first_name TEXT,
                    created_at TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS survey_answers (
                    id          SERIAL PRIMARY KEY,
                    response_id INTEGER NOT NULL,
                    question_id INTEGER NOT NULL,
                    answer_text TEXT
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id         SERIAL PRIMARY KEY,
                    user_id    BIGINT,
                    username   TEXT,
                    first_name TEXT,
                    message    TEXT,
                    created_at TEXT
                )
            """)
        conn.commit()


# ── Users ──────────────────────────────────────────────────────────────────────

def upsert_user(user_id: int, username: str, lang: str):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO users (user_id, username, lang, created_at)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO UPDATE SET
                    username = EXCLUDED.username,
                    lang     = EXCLUDED.lang
            """, (user_id, username or "", lang, now_tashkent()))
        conn.commit()


def all_user_ids() -> list:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id FROM users")
            return [r["user_id"] for r in cur.fetchall()]


def user_count() -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) AS c FROM users")
            return cur.fetchone()["c"]


# ── Portfolio ──────────────────────────────────────────────────────────────────

def add_portfolio_item(category, title, description, file_id, video_url, demo_url) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO portfolio
                    (category, title, description, file_id, video_url, demo_url, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (category, title, description or "", file_id or "",
                  video_url or "", demo_url or "", now_tashkent()))
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


# ── Surveys ────────────────────────────────────────────────────────────────────

def create_survey(title: str) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO surveys (title, is_active, created_at) VALUES (%s, TRUE, %s) RETURNING id",
                (title, now_tashkent())
            )
            row = cur.fetchone()
        conn.commit()
        return row["id"]


def add_survey_question(survey_id: int, text: str, order_num: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO survey_questions (survey_id, text, order_num) VALUES (%s, %s, %s)",
                (survey_id, text, order_num)
            )
        conn.commit()


def get_active_surveys():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM surveys WHERE is_active = TRUE ORDER BY created_at DESC")
            return cur.fetchall()


def get_all_surveys():
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM surveys ORDER BY created_at DESC")
            return cur.fetchall()


def get_survey(survey_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM surveys WHERE id = %s", (survey_id,))
            return cur.fetchone()


def get_survey_questions(survey_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM survey_questions WHERE survey_id = %s ORDER BY order_num",
                (survey_id,)
            )
            return cur.fetchall()


def toggle_survey(survey_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE surveys SET is_active = NOT is_active WHERE id = %s",
                (survey_id,)
            )
        conn.commit()


def delete_survey(survey_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM survey_answers WHERE response_id IN "
                "(SELECT id FROM survey_responses WHERE survey_id = %s)",
                (survey_id,)
            )
            cur.execute("DELETE FROM survey_responses WHERE survey_id = %s", (survey_id,))
            cur.execute("DELETE FROM survey_questions WHERE survey_id = %s", (survey_id,))
            cur.execute("DELETE FROM surveys WHERE id = %s", (survey_id,))
        conn.commit()


def start_response(survey_id: int, user_id: int, username: str, first_name: str) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO survey_responses (survey_id, user_id, username, first_name, created_at)
                VALUES (%s, %s, %s, %s, %s) RETURNING id
            """, (survey_id, user_id, username or "", first_name or "", now_tashkent()))
            row = cur.fetchone()
        conn.commit()
        return row["id"]


def save_answer(response_id: int, question_id: int, answer_text: str):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO survey_answers (response_id, question_id, answer_text) VALUES (%s, %s, %s)",
                (response_id, question_id, answer_text)
            )
        conn.commit()


def get_survey_response_count(survey_id: int) -> int:
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT COUNT(*) AS c FROM survey_responses WHERE survey_id = %s",
                (survey_id,)
            )
            return cur.fetchone()["c"]


def get_survey_responses(survey_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM survey_responses WHERE survey_id = %s ORDER BY created_at DESC",
                (survey_id,)
            )
            return cur.fetchall()


def get_response_answers(response_id: int):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT sa.answer_text, sq.text AS question_text, sq.order_num
                FROM survey_answers sa
                JOIN survey_questions sq ON sa.question_id = sq.id
                WHERE sa.response_id = %s
                ORDER BY sq.order_num
            """, (response_id,))
            return cur.fetchall()


# ── Contacts ───────────────────────────────────────────────────────────────────

def save_contact(user_id: int, username: str, first_name: str, message: str):
    with _conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO contacts (user_id, username, first_name, message, created_at)
                VALUES (%s, %s, %s, %s, %s)
            """, (user_id, username or "", first_name or "", message, now_tashkent()))
        conn.commit()
