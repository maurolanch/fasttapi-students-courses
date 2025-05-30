from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int

class CreationEnrollment(EnrollmentBase):
    pass

class EnrollmentOut(EnrollmentBase):
    id: int
    enrolled_at: datetime

    class Config:
        orm_mode = True

class UpdateEnrollment(EnrollmentBase):
    pass

class EnrollmentDelete(BaseModel):
    id: int