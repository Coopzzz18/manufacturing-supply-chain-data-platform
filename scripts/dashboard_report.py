import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "manufacturing.db"


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

total_shipments = cursor.execute(
    "SELECT COUNT(*) FROM shipments"
).fetchone()[0]

total_production = cursor.execute(
    "SELECT COUNT(*) FROM production"
).fetchone()[0]

inventory_records = cursor.execute(
    "SELECT COUNT(*) FROM inventory"
).fetchone()[0]

products_needing_reorder = cursor.execute(
    "SELECT COUNT(*) FROM inventory WHERE NeedsReorder = 1"
).fetchone()[0]

total_freight = cursor.execute(
    "SELECT SUM(FreightCost) FROM shipments"
).fetchone()[0]

avg_cost_per_unit = cursor.execute(
    "SELECT AVG(CostPerUnit) FROM shipments"
).fetchone()[0]

avg_defect_rate = cursor.execute(
    "SELECT AVG(DefectRate) FROM production"
).fetchone()[0]

top_carrier = cursor.execute("""
    SELECT Carrier, SUM(Units) AS TotalUnits
    FROM shipments
    GROUP BY Carrier
    ORDER BY TotalUnits DESC
    LIMIT 1
""").fetchone()

conn.close()

print("\n=========================================")
print("   Manufacturing Operations Dashboard")
print("=========================================\n")

print(f"Total Shipments:              {total_shipments}")
print(f"Total Production Records:     {total_production}")
print(f"Inventory Records:            {inventory_records}")
print(f"Products Needing Reorder:     {products_needing_reorder}")
print(f"Total Freight Cost:           ${total_freight:,.2f}")
print(f"Average Cost Per Unit:        ${avg_cost_per_unit:.2f}")
print(f"Average Defect Rate:          {avg_defect_rate:.2%}")
print(f"Top Carrier by Units:         {top_carrier[0]} ({top_carrier[1]} units)")