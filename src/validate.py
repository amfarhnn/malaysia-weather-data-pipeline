import pandas as pd


REQUIRED_COLUMNS = [
    "city",
    "latitude",
    "longitude",
    "temperature_c",
    "humidity_percent",
    "precipitation_mm",
    "wind_speed_kmh",
    "weather_time",
    "extracted_at",
    "temperature_category",
    "rain_status",
]


def validate_weather_data(df):
    errors = []

    if df.empty:
        errors.append("DataFrame is empty")

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")

    if errors:
        raise ValueError("; ".join(errors))

    null_columns = df[REQUIRED_COLUMNS].columns[df[REQUIRED_COLUMNS].isnull().any()]
    if len(null_columns) > 0:
        errors.append(f"Columns contain null values: {list(null_columns)}")

    numeric_ranges = {
        "latitude": (-90, 90),
        "longitude": (-180, 180),
        "temperature_c": (-100, 80),
        "humidity_percent": (0, 100),
        "precipitation_mm": (0, None),
        "wind_speed_kmh": (0, None),
    }

    for column, (minimum, maximum) in numeric_ranges.items():
        values = pd.to_numeric(df[column], errors="coerce")

        if values.isnull().any():
            errors.append(f"{column} contains non-numeric values")
            continue

        if minimum is not None and (values < minimum).any():
            errors.append(f"{column} contains values below {minimum}")

        if maximum is not None and (values > maximum).any():
            errors.append(f"{column} contains values above {maximum}")

    for column in ["weather_time", "extracted_at"]:
        parsed_dates = pd.to_datetime(df[column], errors="coerce")
        if parsed_dates.isnull().any():
            errors.append(f"{column} contains invalid datetime values")

    if not df["temperature_category"].isin(["Hot", "Normal"]).all():
        errors.append("temperature_category must be Hot or Normal")

    if not df["rain_status"].isin(["Rain", "No Rain"]).all():
        errors.append("rain_status must be Rain or No Rain")

    if errors:
        raise ValueError("; ".join(errors))

    return True
