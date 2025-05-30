from schemas.enrollment import CreationEnrollment, UpdateEnrollment
from models.enrollment import Enrollment
from sqlalchemy.orm import Session


def create_enrollment(db: Session, enrollment_data: CreationEnrollment):
    new_enrollment = Enrollment(
        student_id = enrollment_data.student_id,
        course_id = enrollment_data.course_id  
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment

def update_enrollment(db: Session, enrollment_id: int, enrollment_data: UpdateEnrollment):
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

    if not enrollment:
        return None
    
    update_data = enrollment_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(enrollment, key, value)
    
    db.commit()
    db.refresh(enrollment)
    return enrollment