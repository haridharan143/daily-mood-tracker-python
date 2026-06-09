import sqlite3

def init_db():
    conn = sqlite3.connect("mood_tracker.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            mood TEXT,
            note TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_mood(date, mood, note):
    conn = sqlite3.connect("mood_tracker.db")
    c = conn.cursor()
    c.execute("INSERT INTO moods (date, mood, note) VALUES (?, ?, ?)", (date, mood, note))
    conn.commit()
    conn.close()

def get_all_moods():
    conn = sqlite3.connect("mood_tracker.db")
    c = conn.cursor()
    c.execute("SELECT * FROM moods ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows
