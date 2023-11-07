from azure.storage.blob import BlobServiceClient, BlobClient
from application.usecase.AzureDataLakeUseCase import AzureDataLakeUseCase
from domain.entity.AzureStorageInputObject import AzureStorageInputObject

class AzureDataLakeUseCaseImpl(AzureDataLakeUseCase):
    def __init__(self, client: BlobServiceClient):
        self.client: BlobServiceClient = client
    
    def create_file_exec(self, container: str, input_object: AzureStorageInputObject):
        blob_client: BlobClient = self.client.get_blob_client(container, input_object.file_name)
        blob_client.upload_blob(
            input_object.blob.model_dump_json(),
            overwrite=True
            )
        return True
    
    def upload_file_exec(self, container: str, input_object: AzureStorageInputObject):
        blob_client: BlobClient = self.client.get_blob_client(container, input_object.file_name)  
        blob_client.upload_blob(
            input_object.blob,
            overwrite=True
            )
        return True