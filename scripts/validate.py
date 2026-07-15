def validate_data(shipments, production, inventory):

    print("\n========== DATA VALIDATION ==========\n")

    print(f"Shipments: {len(shipments)} rows")
    print(f"Production: {len(production)} rows")
    print(f"Inventory: {len(inventory)} rows")

    print("\n----- Missing Values -----")

    print("\nShipments")
    print(shipments.isnull().sum())

    print("\nProduction")
    print(production.isnull().sum())

    print("\nInventory")
    print(inventory.isnull().sum())

    print("\n----- Duplicate Checks -----")

    duplicate_shipments = shipments["ShipmentID"].duplicated().sum()
    duplicate_production = production["ProductionID"].duplicated().sum()
    duplicate_inventory = inventory["InventoryID"].duplicated().sum()

    print(f"Duplicate Shipment IDs : {duplicate_shipments}")
    print(f"Duplicate Production IDs : {duplicate_production}")
    print(f"Duplicate Inventory IDs : {duplicate_inventory}")

    print("\n----- Business Rules -----")

    negative_freight = (shipments["FreightCost"] < 0).sum()
    zero_units = (shipments["Units"] <= 0).sum()
    negative_inventory = (inventory["StockOnHand"] < 0).sum()

    high_defect_rate = (
        production["DefectUnits"] >
        production["UnitsProduced"]
    ).sum()

    print(f"Negative Freight Cost : {negative_freight}")
    print(f"Shipments with Zero Units : {zero_units}")
    print(f"Negative Inventory : {negative_inventory}")
    print(f"Impossible Defect Records : {high_defect_rate}")

    # Inventory Reorder KPI
    needs_reorder = inventory["NeedsReorder"].sum()
    total_inventory = len(inventory)

    if total_inventory > 0:
        percentage = (needs_reorder / total_inventory) * 100
        print(f"Products Needing Reorder : {needs_reorder}")
        print(f"Percent Needing Reorder : {percentage:.2f}%")
    else:
        print("No inventory records found.")

    print("\nValidation Complete")