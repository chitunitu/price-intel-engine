# Price Intel Engine (SQLite + Alerts)

Database-backed price tracker with SQL change detection and price-drop alerts (SQLite + Python).

A database-backed price tracking system that stores price history across runs and detects price changes (drops/rises) using SQL window functions. Built for competitor monitoring and market intelligence workflows.

## What it does
- Creates a SQLite database with two tables: `runs` and `prices`
- Inserts a new “run” each time prices are captured
- Compares the latest run vs the previous run per product
- Flags meaningful price drops (alert logic)

## Tech
- Python 3
- SQLite3
- SQL window functions (`ROW_NUMBER()`)

## Project structure
- `reset_db.py` — creates `market_data.db` + tables and seeds sample data  
- `insert_run_and_prices.py` — inserts a baseline run (3 products)  
- `insert_run_with_changes.py` — inserts another run with simulated price changes (drop/rise)

> Note: `market_data.db` is generated locally and is not committed.

## How to run
```bash
python3 reset_db.py
python3 insert_run_and_prices.py
python3 insert_run_with_changes.py
