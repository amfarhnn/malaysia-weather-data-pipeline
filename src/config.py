import os
from dotenv import load_dotenv, dotenv_values
import urllib.parse


# Load environment and also read .env values explicitly to reflect file edits
load_dotenv()
_env_values = dotenv_values()


class Config:
    AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER_NAME")

    RAW_DATA_PATH = "data/raw/weather_raw.csv"
    PROCESSED_DATA_PATH = "data/processed/weather_cleaned.csv"

    # Prefer values from .env file if present, else fallback to os.environ
    POSTGRES_USER = _env_values.get("POSTGRES_USER") or os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = _env_values.get("POSTGRES_PASSWORD") or os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = _env_values.get("POSTGRES_HOST") or os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = _env_values.get("POSTGRES_PORT") or os.getenv("POSTGRES_PORT")
    POSTGRES_DB = _env_values.get("POSTGRES_DB") or os.getenv("POSTGRES_DB")

    # URL-encode user and password to safely include special characters
    _pg_user = urllib.parse.quote_plus(POSTGRES_USER or "")
    _pg_password = urllib.parse.quote_plus(POSTGRES_PASSWORD or "")

    POSTGRES_URL = (
        f"postgresql+psycopg2://{_pg_user}:{_pg_password}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )