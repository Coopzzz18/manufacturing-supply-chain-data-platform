import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

# --------------------------
# Project Paths
# --------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------
# Sample Data
# --------------------------

plants = [
    "Ontario",
    "Compton",
    "Fresno",
    "Stockton"
]

lines = [
    "Line 1",
    "Line 2",
    "Line 3"
]

products = [
    "Sauce A",
    "Sauce B",
    "Dressing A",
    "Dressing B",
    "Sauce C"
]

# --------------------------
# Generate Production Records
# --------------------------

rows = []

for i in range(1, 2001):

    units = random.randint(500, 3000)

    defects = random.randint(0, 25)

    rows.append({

        "ProductionID": f"P{i:05}",

        "Plant": random.choice(plants),

        "Line": random.choice(lines),

        "Product": random.choice(products),

        "UnitsProduced": units,

        "DefectUnits": defects,

        "ProductionDate": (
            datetime(2026,1,1)
            + timedelta(days=random.randint(0,180))
        )

    })

production = pd.DataFrame(rows)

production.to_csv(
    RAW_DIR / "production.csv",
    index=False
)

print("Production data generated!")

print(f"Rows: {len(production)}")