import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

products = [
    "Sauce A",
    "Sauce B",
    "Dressing A",
    "Dressing B",
    "Sauce C"
]

warehouses = [
    "Long Beach",
    "Ontario",
    "Phoenix",
    "Dallas"
]

rows = []

for i in range(1,1001):

    stock = random.randint(0,6000)

    reorder = random.randint(800,2500)

    rows.append({

        "InventoryID":f"I{i:05}",

        "Product":random.choice(products),

        "Warehouse":random.choice(warehouses),

        "StockOnHand":stock,

        "ReorderLevel":reorder,

        "LastUpdated":(
            datetime(2026,1,1)
            + timedelta(days=random.randint(0,180))
        )

    })

inventory = pd.DataFrame(rows)

inventory.to_csv(
    RAW_DIR / "inventory.csv",
    index=False
)

print("Inventory data generated!")
print(f"Rows: {len(inventory)}")