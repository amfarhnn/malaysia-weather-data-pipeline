import sqlite3
import pandas as pd
from pathlib import Path


def load_weather_data(input_path="data/processed/weather_cleaned.csv"):
    df = pd.read_csv(input_path)

    db_path = Path("weather_pipeline.db")
    conn = sqlite3.connect(db_path)

    df.to_sql(
        "weather_observations",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

    print(f"Data loaded into database: {db_path}")