import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'instance', 'feedforward.db')

# Try both common locations
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(os.path.dirname(__file__), 'feedforward.db')

if not os.path.exists(DB_PATH):
    print("❌ Could not find feedforward.db — check the path and try again.")
    exit(1)

print(f"✅ Found database at: {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Check if column already exists
cursor.execute("PRAGMA table_info(users)")
columns = [row[1] for row in cursor.fetchall()]

if 'allergies' in columns:
    print("✅ Column 'allergies' already exists — nothing to do.")
else:
    cursor.execute("ALTER TABLE users ADD COLUMN allergies VARCHAR(200) DEFAULT ''")
    conn.commit()
    print("✅ Column 'allergies' added successfully!")

conn.close()
print("🎉 Done. Restart your Flask app now.")