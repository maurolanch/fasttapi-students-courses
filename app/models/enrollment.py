from sqlalchemy import Column, Date, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Enrollment(Base):
    __tablename__="enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")