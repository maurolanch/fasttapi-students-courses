from sqlalchemy.orm import Session
from schemas.course import CourseCreation, CourseUpdate
from models.course import Course


def create_course(db: Session, course_data: CourseCreation):
    new_course = Course(
        title = course_data.title,
        description = course_data.description,
        start_date = course_data.start_date,
        end_date = course_data.end_date
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def update_course_by_id(db: Session, course_id: int, course_data: CourseUpdate):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        return None
    
    updated_course = course_data.model_dump(exclude_unset=True)

    for key, value in updated_course.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    return course

def delete_course_by_id(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
        return course
    return None
