from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data


def run_pipeline():
    print("Starting pipeline...")

    shipments, production, inventory = extract_data()
    print("Data extracted.")

    shipments, production, inventory = transform_data(
        shipments,
        production,
        inventory
    )
    print("Data transformed.")

    validate_data(shipments, production, inventory)

    load_data(shipments, production, inventory)

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()