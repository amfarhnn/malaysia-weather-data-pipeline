import pandas as pd


def validate_raw_data(df: pd.DataFrame):
    # Check null values
    assert df["temperature_c"].notnull().all(), "Missing temperature values"
    assert df["humidity_percent"].notnull().all(), "Missing humidity values"

    # Check ranges
    assert (df["humidity_percent"] >= 0).all(), "Invalid humidity < 0"
    assert (df["humidity_percent"] <= 100).all(), "Invalid humidity > 100"

    print("Raw data validation passed")


def validate_processed_data(df: pd.DataFrame):
    # Check duplicates
    assert df.duplicated().sum() == 0, "Duplicates found in processed data"

    # Check categories
    assert df["rain_status"].isin(["Rain", "No Rain"]).all(), "Invalid rain status"

    print("Processed data validation passed")
