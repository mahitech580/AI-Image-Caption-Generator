import sqlite3
from pathlib import Path
from datetime import datetime
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "caption_history.db"
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection
def initialize_database():
    connection = get_connection()
    connection.execute("""CREATE TABLE IF NOT EXISTS caption_history (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT NOT NULL, caption TEXT NOT NULL, processing_time REAL NOT NULL, created_at TEXT NOT NULL)""")
    connection.commit(); connection.close()
def save_caption(filename, caption, processing_time):
    connection = get_connection()
    connection.execute("INSERT INTO caption_history (filename, caption, processing_time, created_at) VALUES (?, ?, ?, ?)", (filename, caption, processing_time, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit(); connection.close()
def get_history():
    connection = get_connection(); rows = connection.execute("SELECT id, filename, caption, processing_time, created_at FROM caption_history ORDER BY id DESC").fetchall(); connection.close(); return [dict(row) for row in rows]
def delete_caption(caption_id):
    connection = get_connection(); cursor = connection.execute("DELETE FROM caption_history WHERE id = ?", (caption_id,)); connection.commit(); deleted = cursor.rowcount > 0; connection.close(); return deleted
