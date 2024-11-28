import os
import streamlit
from azure.storage.blob import BlobServiceClient
from utils.Config import Config


def upload_blob(file, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)

    bloc_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)

    bloc_client.upload_blob(file, overwrite=True)

    return bloc_client.url
