from sqlalchemy.orm import Session
from schemas.student import StudentCreation
from models.student import Student

def create_student(db: Session, student_data: StudentCreation):
    new_student = Student(
        name = student_data.name,
        email = student_data.email
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


