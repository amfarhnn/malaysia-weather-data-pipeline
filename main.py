from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data
from src.logger import setup_logger


def run_pipeline():
    logger = setup_logger()

    try:
        logger.info("Pipeline started")

        extract_weather_data()
        logger.info("Data extraction completed")

        transform_weather_data()
        logger.info("Data transformation completed")

        load_weather_data()
        logger.info("Data loading completed")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        print("Error occurred. Check logs/pipeline.log")


if __name__ == "__main__":
    run_pipeline()