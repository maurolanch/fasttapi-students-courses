from sqlalchemy.orm import Session
from schemas.student import StudentCreation, StudentUpdate
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

def update_student_by_id(db: Session, student_id: int, student_update: StudentUpdate):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None
    
    update_data = student_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

def delete_student_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None
    else:
        db.delete(student)
        db.commit()
    return student


