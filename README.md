# Malaysia Weather Data Pipeline

Weather API -> Python -> Raw CSV -> Cleaned CSV -> SQLite Database

## Cloud Architecture

This project uses Azure Blob Storage as a data lake with partitioned storage:

- Raw data is stored in hierarchical folders by date
- Processed data is stored in a structured format for analytics
- Supports scalable data ingestion and retrieval

### Data Flow

API -> Python ETL -> Raw Layer (Azure) -> Processed Layer (Azure) -> SQLite

## Docker

This project can be containerized using Docker.

### Build Image

```bash
docker build -t malaysia-weather-pipeline .
```

### Run Container

```bash
docker run --env-file .env malaysia-weather-pipeline
```