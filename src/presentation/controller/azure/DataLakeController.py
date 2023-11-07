from azure.storage.blob import BlobServiceClient, BlobSasPermissions
from presentation.schema.AzureSchema import CreateFileFormObject, UploadFileFormObject
from application.usecase.AzureDataLakeUseCase import AzureDataLakeUseCase
from application.usecase.implements.AzureDataLakeUseCaseImpl import AzureDataLakeUseCaseImpl
from domain.entity.AzureStorageInputObject import AzureStorageInputObject, AzureStorageDictBlob
from infrastructure.azure.utils.AzureConstants import AzureConstants
from infrastructure.azure.utils.AzureStorageClientWithUserDelegationSAS import AzureStorageClientWithUserDelegationSAS

class DI:    
    
    @staticmethod
    def azure_datalake_usecase_with_user_delegation_sas(
        container: str,
        permissions=BlobSasPermissions(
            read=True,
            add=True,
            write=True,
            create=True,
            execute=True
            )
        ):
        """
        ユーザ委任SASを使ってUsecaseを生成する
        """

        client: BlobServiceClient = AzureStorageClientWithUserDelegationSAS.get_service_client(
            AzureConstants.STORAGE_ACCOUNT_NAME,
            container,
            permissions=permissions,
        )
        usecase: AzureDataLakeUseCase = AzureDataLakeUseCaseImpl(
            client,
            )
        return usecase
    
    
class DataLakeController:
    
    def __init__(self):
        pass
    
    
    def create_file(self, container: str, form: CreateFileFormObject):
        """
        ファイルを作成する

        """
        usecase = DI.azure_datalake_usecase_with_user_delegation_sas(container)
        return usecase.create_file_exec(
            container=container,
            input_object=AzureStorageInputObject(
                file_name=form.file_name,
                blob=AzureStorageDictBlob(
                    company_id=form.blob.company_id,
                    type=form.blob.type,
                    data=form.blob.data,
                )
            )
        )
        
    def upload_file(self, container: str, form: UploadFileFormObject):
        """
        ファイルをアップロードする

        """
        usecase = DI.azure_datalake_usecase_with_user_delegation_sas(container)
        return usecase.upload_file_exec(
            container=container,
            input_object=AzureStorageInputObject(
                file_name=form.file_name,
                blob=form.blob,
            )
        )