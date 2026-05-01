import pandas as pd
from sqlalchemy import create_engine, text
from src.config import Config


def get_last_timestamp(engine):
    query = text("SELECT MAX(extracted_at) FROM weather_observations")
    with engine.connect() as connection:
        result = connection.execute(query).scalar()
    return result


def load_weather_data(input_path=Config.PROCESSED_DATA_PATH):
    df = pd.read_csv(input_path)
    df["extracted_at"] = pd.to_datetime(df["extracted_at"])

    engine = create_engine(Config.POSTGRES_URL)

    try:
        last_timestamp = get_last_timestamp(engine)
    except Exception:
        last_timestamp = None

    if last_timestamp is not None:
        df = df[df["extracted_at"] > pd.to_datetime(last_timestamp)]

    if df.empty:
        print("No new data to insert")
        return

    df.to_sql(
        "weather_observations",
        engine,
        if_exists="append",
        index=False
    )

    print(f"{len(df)} new records inserted into PostgreSQL")