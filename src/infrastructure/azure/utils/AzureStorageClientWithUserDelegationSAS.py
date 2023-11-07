import datetime
from azure.storage.blob import BlobServiceClient, generate_container_sas, UserDelegationKey, BlobSasPermissions
from azure.identity import DefaultAzureCredential

class AzureStorageClientWithUserDelegationSAS:
        
    @staticmethod
    def get_service_client(account_name: str, container_name: str, permissions: BlobSasPermissions = BlobSasPermissions()):
        
        account_url = 'https://{}.blob.core.windows.net/'.format(
            account_name
        )
                
        # 有効期限(1hour)
        start_time = datetime.datetime.now(datetime.timezone.utc)
        expiry_time = start_time + datetime.timedelta(hours=1)
        
        # ユーザ委任キーの作成するために一時的に作成する
        tmp_service_client: BlobServiceClient = BlobServiceClient(
            account_url=account_url,
            credential=DefaultAzureCredential()
        )
            
        
        # ユーザ委任キーの作成
        user_delegation_key: UserDelegationKey = tmp_service_client.get_user_delegation_key(
            key_start_time=datetime.datetime.now(datetime.timezone.utc),
            key_expiry_time=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        )
        
        # コンテナに対するユーザ委任SASトークンの作成
        sas_token = generate_container_sas(
            account_name=account_name,
            container_name=container_name,
            permission=permissions,
            user_delegation_key=user_delegation_key,
            expiry=expiry_time,
            start=start_time
        )

        return BlobServiceClient(
            account_url=account_url,
            credential=sas_token
            )
