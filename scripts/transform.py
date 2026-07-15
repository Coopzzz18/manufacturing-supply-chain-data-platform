def transform_data(shipments, production, inventory):

    # --------------------------
    # Remove duplicate rows
    # --------------------------
    shipments = shipments.drop_duplicates()
    production = production.drop_duplicates()
    inventory = inventory.drop_duplicates()

    # --------------------------
    # Convert date columns
    # --------------------------
    shipments["ShipDate"] = shipments["ShipDate"].astype("datetime64[ns]")
    production["ProductionDate"] = production["ProductionDate"].astype("datetime64[ns]")
    inventory["LastUpdated"] = inventory["LastUpdated"].astype("datetime64[ns]")

    # --------------------------
    # Standardize text columns
    # --------------------------
    shipments["Customer"] = shipments["Customer"].str.strip().str.title()
    shipments["Carrier"] = shipments["Carrier"].str.strip().str.upper()
    shipments["Product"] = shipments["Product"].str.strip().str.title()

    production["Product"] = production["Product"].str.strip().str.title()
    production["Plant"] = production["Plant"].str.strip().str.title()

    inventory["Product"] = inventory["Product"].str.strip().str.title()
    inventory["Warehouse"] = inventory["Warehouse"].str.strip().str.title()

    # --------------------------
    # Add business KPI columns
    # --------------------------
    shipments["CostPerUnit"] = shipments["FreightCost"] / shipments["Units"]
    production["DefectRate"] = production["DefectUnits"] / production["UnitsProduced"]
    inventory["NeedsReorder"] = inventory["StockOnHand"] < inventory["ReorderLevel"]

    return shipments, production, inventory