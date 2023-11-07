import os
from dotenv import load_dotenv

load_dotenv()

class AzureConstants:
    STORAGE_ACCOUNT_NAME: str = os.environ.get('AZURE_STORAGE_ACCOUNT_NAME')
    TENANT_ID: str = os.environ.get('AZURE_TENANT_ID')
    CLIENT_ID: str = os.environ.get('AZURE_CLIENT_ID')
    CLIENT_SECRET: str = os.environ.get('AZURE_CLIENT_SECRET')