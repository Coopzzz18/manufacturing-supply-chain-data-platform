import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "manufacturing.db"


def load_data(shipments, production, inventory):

    DB_DIR.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    shipments.to_sql("shipments", conn, if_exists="replace", index=False)
    production.to_sql("production", conn, if_exists="replace", index=False)
    inventory.to_sql("inventory", conn, if_exists="replace", index=False)

    conn.close()

    print("Data loaded into SQLite successfully.")