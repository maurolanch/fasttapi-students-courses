from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__="courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")