DROP VIEW IF EXISTS carrier_summary;

CREATE VIEW carrier_summary AS
SELECT
    Carrier,
    COUNT(*) AS TotalShipments,
    SUM(Units) AS TotalUnits,
    SUM(FreightCost) AS TotalFreightCost,
    AVG(CostPerUnit) AS AvgCostPerUnit
FROM shipments
GROUP BY Carrier;


DROP VIEW IF EXISTS inventory_reorder_summary;

CREATE VIEW inventory_reorder_summary AS
SELECT
    Warehouse,
    COUNT(*) AS InventoryRecords,
    SUM(CASE WHEN NeedsReorder = 1 THEN 1 ELSE 0 END) AS ProductsNeedingReorder
FROM inventory
GROUP BY Warehouse;


DROP VIEW IF EXISTS production_summary;

CREATE VIEW production_summary AS
SELECT
    Plant,
    Line,
    COUNT(*) AS ProductionRecords,
    SUM(UnitsProduced) AS TotalUnitsProduced,
    SUM(DefectUnits) AS TotalDefects,
    AVG(DefectRate) AS AvgDefectRate
FROM production
GROUP BY Plant, Line;