import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER_NAME")

    RAW_DATA_PATH = "data/raw/weather_raw.csv"
    PROCESSED_DATA_PATH = "data/processed/weather_cleaned.csv"