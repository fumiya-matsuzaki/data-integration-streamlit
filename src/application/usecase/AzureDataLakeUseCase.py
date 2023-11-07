from abc import abstractmethod
from domain.entity.AzureStorageInputObject import AzureStorageInputObject


class AzureDataLakeUseCase:
        
    @abstractmethod
    def create_file_exec(self, container: str, input_object: AzureStorageInputObject):
        raise NotImplementedError
    
    @abstractmethod
    def upload_file_exec(self, container: str, input_object: AzureStorageInputObject):
        raise NotImplementedError

    