"""
Run ONCE from your project root to add notifications and messages tables.
    python migrate_inbox.py
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'feedforward.db')
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(os.path.dirname(__file__), 'feedforward.db')
if not os.path.exists(DB_PATH):
    print("❌ Could not find feedforward.db"); exit(1)

print(f"✅ Found database at: {DB_PATH}")
conn   = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
existing = {r[0] for r in cursor.fetchall()}

if 'notifications' not in existing:
    cursor.execute("""
        CREATE TABLE notifications (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL REFERENCES users(id),
            type       VARCHAR(50),
            title      VARCHAR(200),
            body       VARCHAR(500),
            link       VARCHAR(300),
            is_read    BOOLEAN DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("✅ Created 'notifications' table")
else:
    print("ℹ️  'notifications' table already exists")

if 'messages' not in existing:
    cursor.execute("""
        CREATE TABLE messages (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id   INTEGER NOT NULL REFERENCES users(id),
            receiver_id INTEGER NOT NULL REFERENCES users(id),
            listing_id  INTEGER REFERENCES food_listings(id),
            body        TEXT NOT NULL,
            is_read     BOOLEAN DEFAULT 0,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("✅ Created 'messages' table")
else:
    print("ℹ️  'messages' table already exists")

conn.commit()
conn.close()
print("🎉 Done. Restart your Flask app now.")