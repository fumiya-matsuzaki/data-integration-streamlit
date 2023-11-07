from pydantic import BaseModel

class AbsEntity(BaseModel):
    class Config:
        frozen = True
        orm_mode = True
        from_attributes = True
        arbitrary_types_allowed = True
        validate_assignment = True