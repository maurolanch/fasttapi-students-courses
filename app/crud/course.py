from sqlalchemy.orm import Session
from schemas.course import CourseCreation, CourseUpdate
from models.course import Course


def create_course(db: Session, course_data: CourseCreation):
    new_course = Course(
        title = course_data.title,
        descrption = course_data.description,
        start_date = course_data.start_date,
        end_date = course_data.end_date
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


def update_course_by_id(db: Session, course_id: int, course_data: CourseUpdate):
    pass

