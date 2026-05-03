import pandas as pd
from sqlalchemy import create_engine, text
from src.config import Config


def load_weather_data(input_path="data/processed/weather_cleaned.csv"):
    df = pd.read_csv(input_path)

    engine = create_engine(Config.POSTGRES_URL)

    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS weather_observations (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100),
                latitude FLOAT,
                longitude FLOAT,
                temperature_c FLOAT,
                humidity_percent FLOAT,
                precipitation_mm FLOAT,
                wind_speed_kmh FLOAT,
                weather_time TIMESTAMP,
                extracted_at TIMESTAMP,
                temperature_category VARCHAR(50),
                rain_status VARCHAR(50),
                UNIQUE(city, weather_time, extracted_at)
            );
        """))

    df.to_sql(
        "weather_observations",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print("Data loaded into PostgreSQL database.")