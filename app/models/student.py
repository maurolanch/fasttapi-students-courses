from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Student(Base):
    __tablename__="students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True, index=True)
    registration_date = Column(DateTime(timezone=True), server_default= func.now())


    enrollments = relationship("Enrollment", back_populates="student")