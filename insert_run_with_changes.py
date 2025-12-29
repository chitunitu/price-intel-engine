import sqlite3
from datetime import datetime

DB_NAME = "market_data.db"

# Simulate new prices (some change)
NEW_PRICES = {
    "A Light in the Attic": 49.99,   # drop
    "Tipping the Velvet": 55.10,     # rise
    "Soumission": 50.10              # same
}

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# Create a new run
cur.execute("INSERT INTO runs (note) VALUES (?)", (f"simulated changes {datetime.now()}",))
run_id = cur.lastrowid

# Insert changed prices for each product
for product, new_price in NEW_PRICES.items():
    cur.execute("""
        INSERT INTO prices (product, price, currency, source, url, run_id)
        SELECT product, ?, currency, source, url, ?
        FROM prices
        WHERE product = ?
        ORDER BY run_id DESC
        LIMIT 1
    """, (new_price, run_id, product))

conn.commit()
conn.close()

print(f"Inserted run_id={run_id} with simulated price changes.")
