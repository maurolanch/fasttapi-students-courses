from pydantic import BaseModel, EmailStr
from datetime import datetime

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreation(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    registration_date: datetime

    class Config:
        orm_mode = True

class StudentDelete(BaseModel):
    id: int

