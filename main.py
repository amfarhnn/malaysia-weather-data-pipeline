from datetime import datetime

from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data
from src.logger import setup_logger
from src.upload_to_azure import upload_file_to_azure
from src.config import Config
from src.validate import validate_raw_data, validate_processed_data


def run_pipeline():
    logger = setup_logger()
    now = datetime.now()
    date_path = f"year={now.year}/month={now.month:02d}/day={now.day:02d}"

    raw_blob_name = f"raw/{date_path}/weather_raw_{now.strftime('%H%M%S')}.csv"
    processed_blob_name = (
        f"processed/{date_path}/weather_cleaned_{now.strftime('%H%M%S')}.csv"
    )

    try:
        logger.info("Pipeline started")

        # Extract
        raw_df = extract_weather_data()
        logger.info("Data extraction completed")

        # Validate raw data
        validate_raw_data(raw_df)

        # Upload raw
        upload_file_to_azure(
            Config.RAW_DATA_PATH,
            raw_blob_name
        )
        logger.info("Raw data uploaded to Azure Blob Storage")

        # Transform
        processed_df = transform_weather_data()
        logger.info("Data transformation completed")

        # Validate processed data
        validate_processed_data(processed_df)

        # Upload processed
        upload_file_to_azure(
            Config.PROCESSED_DATA_PATH,
            processed_blob_name
        )
        logger.info("Processed data uploaded to Azure Blob Storage")

        # Load
        load_weather_data()
        logger.info("Data loading completed")

        logger.info("Pipeline completed successfully")
        print("Pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print("Error occurred. Check logs/pipeline.log")


if __name__ == "__main__":
    run_pipeline()