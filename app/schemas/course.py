from pydantic import BaseModel
from datetime import date
from typing import Optional


class CourseBase(BaseModel):
    title: str
    description: str | None = None
    start_date: date
    end_date: date

class CourseCreation(CourseBase):
    pass


class CourseOut(CourseBase):
    id: int

    class Config:
        orm_mode = True
    
class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None