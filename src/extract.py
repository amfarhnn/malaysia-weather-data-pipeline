import requests
import pandas as pd
from datetime import datetime
from pathlib import Path


CITIES = {
    "Kuala Lumpur": {"lat": 3.1390, "lon": 101.6869},
    "Selangor": {"lat": 3.0738, "lon": 101.5183},
    "Penang": {"lat": 5.4164, "lon": 100.3327},
    "Johor Bahru": {"lat": 1.4927, "lon": 103.7414},
    "Kota Bharu": {"lat": 6.1254, "lon": 102.2381},
    "Kuantan": {"lat": 3.8077, "lon": 103.3260},
    "Kuching": {"lat": 1.5533, "lon": 110.3592},
    "Kota Kinabalu": {"lat": 5.9804, "lon": 116.0735},
}


def extract_weather_data():
    records = []

    for city, coord in CITIES.items():
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={coord['lat']}"
            f"&longitude={coord['lon']}"
            "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current"]

        records.append({
            "city": city,
            "latitude": coord["lat"],
            "longitude": coord["lon"],
            "temperature_c": current.get("temperature_2m"),
            "humidity_percent": current.get("relative_humidity_2m"),
            "precipitation_mm": current.get("precipitation"),
            "wind_speed_kmh": current.get("wind_speed_10m"),
            "weather_time": current.get("time"),
            "extracted_at": datetime.now().isoformat()
        })

    df = pd.DataFrame(records)

    output_path = Path("data/raw/weather_raw.csv")
    df.to_csv(output_path, index=False)

    print(f"Raw data saved: {output_path}")
    return df