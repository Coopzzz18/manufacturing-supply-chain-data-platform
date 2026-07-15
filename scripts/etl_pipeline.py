import pandas as pd
import sqlite3
from pathlib import Path

# Folder paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
CLEANED_DIR = BASE_DIR / "data" / "cleaned"
DB_PATH = BASE_DIR / "database" / "manufacturing.db"

# Extract
shipments = pd.read_csv(RAW_DIR / "shipments.csv")
production = pd.read_csv(RAW_DIR / "production.csv")
inventory = pd.read_csv(RAW_DIR / "inventory.csv")

# Transform
shipments["ShipDate"] = pd.to_datetime(shipments["ShipDate"])
production["ProductionDate"] = pd.to_datetime(production["ProductionDate"])
inventory["LastUpdated"] = pd.to_datetime(inventory["LastUpdated"])

shipments["Customer"] = shipments["Customer"].str.strip().str.title()
shipments["Carrier"] = shipments["Carrier"].str.strip().str.upper()

production["Product"] = production["Product"].str.strip().str.title()
inventory["Product"] = inventory["Product"].str.strip().str.title()

shipments["CostPerUnit"] = shipments["FreightCost"] / shipments["Units"]
production["DefectRate"] = production["DefectUnits"] / production["UnitsProduced"]

inventory["NeedsReorder"] = inventory["StockOnHand"] < inventory["ReorderLevel"]

# Save cleaned files
shipments.to_csv(CLEANED_DIR / "cleaned_shipments.csv", index=False)
production.to_csv(CLEANED_DIR / "cleaned_production.csv", index=False)
inventory.to_csv(CLEANED_DIR / "cleaned_inventory.csv", index=False)

# Load into SQLite
conn = sqlite3.connect(DB_PATH)

shipments.to_sql("shipments", conn, if_exists="replace", index=False)
production.to_sql("production", conn, if_exists="replace", index=False)
inventory.to_sql("inventory", conn, if_exists="replace", index=False)

conn.close()

print("ETL pipeline completed successfully.")
print("Cleaned CSV files saved.")
print("SQLite database created.")