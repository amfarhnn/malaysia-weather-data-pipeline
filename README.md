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
```

## Tech Stack

- Python
- Pandas
- REST API
- Azure Blob Storage
- SQLite
- Docker
- Python Scheduler
- Power BI
- Git & GitHub

## Key Features

- Extracts real-time weather data from multiple Malaysian cities
- Implements an end-to-end ETL pipeline
- Stores raw and processed data in Azure Blob Storage
- Uses partitioned data lake structure by year, month, and day
- Loads processed data into SQLite database
- Includes logging for pipeline monitoring
- Supports automated scheduling
- Containerized using Docker
- Provides dashboard visualization using Power BI

## Data Lake Structure

```
weather-data/
│
├── raw/
│   └── year=2026/month=04/day=29/
│       └── weather_raw_HHMMSS.csv
│
└── processed/
    └── year=2026/month=04/day=29/
        └── weather_cleaned_HHMMSS.csv
```

## Dataset Fields

| Column | Description |
|--------|-------------|
| city | Malaysian city name |
| latitude | City latitude |
| longitude | City longitude |
| temperature_c | Temperature in Celsius |
| humidity_percent | Relative humidity percentage |
| precipitation_mm | Precipitation level |
| wind_speed_kmh | Wind speed |
| weather_time | Weather observation time |
| extracted_at | Data extraction timestamp |
| temperature_category | Hot or Normal classification |
| rain_status | Rain or No Rain classification |

## Project Structure

```
malaysia-weather-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── upload_to_azure.py
│
├── main.py
├── scheduler.py
├── check_db.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run Locally

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

```
AZURE_STORAGE_CONNECTION_STRING=your_azure_connection_string
AZURE_CONTAINER_NAME=weather-data
```

### 5. Run pipeline

```bash
python main.py
```

## Run with Docker

### Build Docker image

```bash
docker build -t weather-pipeline .
```

### Run Docker container

```bash
docker run --env-file .env weather-pipeline
```

## Run Scheduler

```bash
python scheduler.py
```

The scheduler automates pipeline execution and simulates workflow orchestration similar to Apache Airflow.

## Dashboard

The Power BI dashboard visualizes:

- Temperature by city
- Humidity by city
- Rain status distribution
- Weather trend over time

![Power BI Dashboard](screenshots/powerbi_dashboard.png)

## Challenges & Solutions

During development, Docker setup required troubleshooting due to Windows virtualization and WSL2 configuration issues.

**Actions taken:**

- Enabled SVM Mode in BIOS
- Installed and configured WSL2 with Ubuntu
- Updated WSL kernel
- Reinstalled Docker Desktop cleanly
- Verified Docker Engine and container execution

This improved understanding of containerization, virtualization, and local development environments.

## Skills Demonstrated

- Data ingestion
- ETL pipeline development
- Cloud storage integration
- Data lake architecture
- Data transformation
- SQL database loading
- Workflow automation
- Docker containerization
- Dashboard reporting
- GitHub project documentation

## Resume Summary

Built a Dockerized end-to-end data engineering pipeline using Python, Azure Blob Storage, SQLite, and Power BI. The pipeline extracts real-time weather data from a public API, stores raw and processed datasets in a partitioned cloud data lake, loads structured data into a database, supports automated scheduling, and provides dashboard analytics.

## Future Improvements

- Replace SQLite with PostgreSQL or Azure SQL Database
- Add Apache Airflow for orchestration
- Add automated data quality checks
- Deploy pipeline to Azure Container Apps
- Add CI/CD using GitHub Actions
