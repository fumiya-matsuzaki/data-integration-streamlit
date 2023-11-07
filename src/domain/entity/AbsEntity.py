from pydantic import BaseModel

class AbsEntity(BaseModel):
    class Config:
        frozen = True
        from_attributes = True
        arbitrary_types_allowed = True
        validate_assignment = True