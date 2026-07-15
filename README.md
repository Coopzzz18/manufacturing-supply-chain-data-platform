# Manufacturing Supply Chain Data Platform

An end-to-end data engineering and business intelligence project that simulates manufacturing, shipping, and inventory operations.

## Project Overview

This project generates realistic manufacturing supply chain data, processes it through a modular ETL pipeline, validates data quality, loads the cleaned data into SQLite, creates reusable SQL views, and exports reporting datasets for Power BI.

## Architecture

```text
Python Data Generators
        ↓
Raw CSV Files
        ↓
Extract
        ↓
Transform
        ↓
Validate
        ↓
SQLite Database
        ↓
SQL Views
        ↓
Power BI Dashboard