import pandas as pd
from pathlib import Path


def transform_weather_data(input_path="data/raw/weather_raw.csv"):
    df = pd.read_csv(input_path)

    df["weather_time"] = pd.to_datetime(df["weather_time"])
    df["extracted_at"] = pd.to_datetime(df["extracted_at"])

    df["temperature_category"] = df["temperature_c"].apply(
        lambda x: "Hot" if x >= 30 else "Normal"
    )

    df["rain_status"] = df["precipitation_mm"].apply(
        lambda x: "Rain" if x > 0 else "No Rain"
    )

    df = df.drop_duplicates()

    output_path = Path("data/processed/weather_cleaned.csv")
    df.to_csv(output_path, index=False)

    print(f"Cleaned data saved: {output_path}")
    return df