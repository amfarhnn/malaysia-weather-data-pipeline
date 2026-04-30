# Malaysia Weather Data Engineering Pipeline

An end-to-end cloud-based data engineering project that extracts real-time weather data from multiple Malaysian cities, transforms the data using Python, stores raw and processed data in Azure Blob Storage, loads structured data into SQLite, and visualizes insights using Power BI.

---

## Project Overview

This project simulates a real-world data engineering workflow involving API ingestion, ETL processing, cloud data lake storage, database loading, scheduling, containerization, and dashboard reporting.

The project was built to demonstrate practical data engineering skills for internship and entry-level data roles.

---

## Architecture

```text
Open-Meteo API
      ↓
Python Extract
      ↓
Raw CSV
      ↓
Azure Blob Storage - Raw Layer
      ↓
Python Transform
      ↓
Processed CSV
      ↓
Azure Blob Storage - Processed Layer
      ↓
SQLite Database
      ↓
Power BI Dashboard

