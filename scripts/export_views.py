import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "manufacturing.db"
REPORT_DATA_DIR = BASE_DIR / "reports" / "power_bi_data"


def export_view(connection, view_name):
    query = f"SELECT * FROM {view_name};"
    dataframe = pd.read_sql_query(query, connection)

    output_path = REPORT_DATA_DIR / f"{view_name}.csv"
    dataframe.to_csv(output_path, index=False)

    print(f"Exported {view_name}: {len(dataframe)} rows")
    print(f"Saved to: {output_path}")


def export_power_bi_data():
    REPORT_DATA_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as connection:
        export_view(connection, "carrier_summary")
        export_view(connection, "inventory_reorder_summary")
        export_view(connection, "production_summary")

    print("\nPower BI data export completed successfully!")


if __name__ == "__main__":
    export_power_bi_data()