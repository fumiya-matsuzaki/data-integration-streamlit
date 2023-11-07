from pydantic import BaseModel
    
class DictBlob(BaseModel):
    company_id: str
    type: str
    data: dict
    
class BytesBlob(BaseModel):
    bytes_data: bytes

class UploadFileFormObject(BaseModel):
    file_name: str
    blob: BytesBlob

class CreateFileFormObject(BaseModel):
    file_name: str
    blob: DictBlob