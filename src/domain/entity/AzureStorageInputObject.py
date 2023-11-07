from domain.entity.AbsEntity import AbsEntity


class AzureStorageDictBlob(AbsEntity):
    company_id: str
    type: str
    data: dict


class AzureStorageInputObject(AbsEntity):
    file_name: str
    blob: AzureStorageDictBlob or bytes