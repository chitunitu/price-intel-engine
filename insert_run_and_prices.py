import sqlite3

conn = sqlite3.connect("market_data.db")
cur = conn.cursor()

# 1) Create a run record
cur.execute("INSERT INTO runs (note) VALUES (?)", ("manual test run",))
run_id = cur.lastrowid

# 2) Insert prices tied to this run_id
data = [
    ("A Light in the Attic", 51.77, "books.toscrape.com", run_id),
    ("Tipping the Velvet", 53.74, "books.toscrape.com", run_id),
    ("Soumission", 50.10, "books.toscrape.com", run_id),
]

cur.executemany("""
INSERT INTO prices (product, price, source, run_id)
VALUES (?, ?, ?, ?)
""", data)

conn.commit()
conn.close()

print(f"Inserted run_id={run_id} with {len(data)} prices")
