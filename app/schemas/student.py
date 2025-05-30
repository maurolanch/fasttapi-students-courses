from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

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

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class StudentDelete(BaseModel):
    id: int

