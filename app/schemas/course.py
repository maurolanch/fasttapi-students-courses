from pydantic import BaseModel
from datetime import date


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

class CourseDelete(BaseModel):
    id: int