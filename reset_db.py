import sqlite3

DB_NAME = "market_data.db"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# Drop old tables if they exist (safe reset)
cur.execute("DROP TABLE IF EXISTS prices;")
cur.execute("DROP TABLE IF EXISTS runs;")

# Recreate tables
cur.execute("""
CREATE TABLE runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT,
    started_at TEXT DEFAULT (datetime('now'))
);
""")

cur.execute("""
CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    price REAL NOT NULL,
    currency TEXT DEFAULT '£',
    source TEXT,
    url TEXT,
    run_id INTEGER NOT NULL,
    timestamp TEXT DEFAULT (datetime('now')),
    FOREIGN KEY(run_id) REFERENCES runs(run_id)
);
""")

# Seed one run + 3 sample prices
cur.execute("INSERT INTO runs (note) VALUES (?)", ("seed run",))
run_id = cur.lastrowid

seed = [
    ("A Light in the Attic", 51.77, "£", "books.toscrape.com", "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", run_id),
    ("Tipping the Velvet", 53.74, "£", "books.toscrape.com", "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html", run_id),
    ("Soumission", 50.10, "£", "books.toscrape.com", "https://books.toscrape.com/catalogue/soumission_998/index.html", run_id),
]

cur.executemany("""
INSERT INTO prices (product, price, currency, source, url, run_id)
VALUES (?, ?, ?, ?, ?, ?)
""", seed)

conn.commit()
conn.close()

print("✅ Reset complete: market_data.db created with tables runs + prices and seeded data.")
