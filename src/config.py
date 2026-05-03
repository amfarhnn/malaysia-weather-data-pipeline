import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER_NAME")

    RAW_DATA_PATH = "data/raw/weather_raw.csv"
    PROCESSED_DATA_PATH = "data/processed/weather_cleaned.csv"
    # Helper to treat missing or literal 'None' values as absent
    @staticmethod
    def _env(name, default=None):
        v = os.getenv(name)
        if v is None:
            return default
        s = str(v).strip()
        if s == "" or s.lower() == "none":
            return default
        return s

    POSTGRES_HOST = _env("POSTGRES_HOST") or "localhost"
    POSTGRES_PORT = _env("POSTGRES_PORT") or "5432"
    POSTGRES_DB = _env("POSTGRES_DB") or "weather_db"
    POSTGRES_USER = _env("POSTGRES_USER") or "postgres"
    POSTGRES_PASSWORD = _env("POSTGRES_PASSWORD") or "postgres"

    POSTGRES_URL = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )