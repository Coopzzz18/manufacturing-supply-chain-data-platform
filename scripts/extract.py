import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"


def extract_data():

    shipments = pd.read_csv(RAW_DIR / "shipments.csv")
    production = pd.read_csv(RAW_DIR / "production.csv")
    inventory = pd.read_csv(RAW_DIR / "inventory.csv")

    return shipments, production, inventory