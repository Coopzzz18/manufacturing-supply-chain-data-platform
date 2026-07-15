import pandas as pd
import random
from pathlib import Path
from datetime import datetime, timedelta

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

# Sample values
customers = ["Burger King", "Walmart", "Costco", "Target", "Kroger", "Aldi"]
carriers = ["MSC", "MAERSK", "CMA CGM", "UPS", "FedEx"]
destinations = ["Australia", "Texas", "California", "Nevada", "Arizona", "Florida"]
statuses = ["On Time", "Late", "Delayed"]
products = ["Sauce A", "Sauce B", "Dressing A", "Dressing B", "Sauce C"]

# Make sure raw folder exists
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Generate shipment data
shipment_rows = []

for i in range(1, 501):
    units = random.randint(100, 2500)
    freight_cost = round(units * random.uniform(1.50, 4.75), 2)

    shipment_rows.append({
        "ShipmentID": f"S{i:05}",
        "OrderID": f"O{i:05}",
        "Customer": random.choice(customers),
        "Carrier": random.choice(carriers),
        "Destination": random.choice(destinations),
        "ShipDate": datetime(2026, 1, 1) + timedelta(days=random.randint(0, 180)),
        "Units": units,
        "FreightCost": freight_cost,
        "Status": random.choice(statuses),
        "Product": random.choice(products)
    })

shipments = pd.DataFrame(shipment_rows)

# Save CSV
shipments.to_csv(RAW_DIR / "shipments.csv", index=False)

print("Generated shipments.csv successfully.")
print(f"Rows created: {len(shipments)}")
print(f"Saved to: {RAW_DIR / 'shipments.csv'}")