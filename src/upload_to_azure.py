from pathlib import Path

from azure.storage.blob import BlobServiceClient
from src.config import Config


def upload_file_to_azure(local_file_path, blob_name):
    if not Config.AZURE_CONNECTION_STRING:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing in .env")

    if not Config.AZURE_CONTAINER:
        raise ValueError("AZURE_CONTAINER_NAME is missing in .env")

    blob_service_client = BlobServiceClient.from_connection_string(
        Config.AZURE_CONNECTION_STRING
    )

    blob_client = blob_service_client.get_blob_client(
        container=Config.AZURE_CONTAINER,
        blob=blob_name
    )

    with open(Path(local_file_path), "rb") as file:
        blob_client.upload_blob(file, overwrite=True)

    print(f"Uploaded to Azure: {blob_name}")