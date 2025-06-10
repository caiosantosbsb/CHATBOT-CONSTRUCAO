import sqlite3
import pandas as pd

DB_PATH = 'database.db'

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
);
"""


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)
    conn.close()

if __name__ == '__main__':
    init_db()
    print('Database initialized')
