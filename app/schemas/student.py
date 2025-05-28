from pydantic import BaseModel
from datetime import datetime

class Student(BaseModel):
        id: int
        name: str
        email: str
        registration_date: datetime


