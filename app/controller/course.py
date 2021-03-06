from app.models import *
from app import *
from sqlalchemy import *

def learning():
    topics = get_topic()

    result = {
        "topic" : []
    }
    for tp in topics :
        result["topic"].append({
            "name" : tp.topic_name,
            "link" : "/Learning/" + str(tp.id),
            "id"   : tp.id
        })
    return result, len(topics)

def get_topic():
    topic = Topic.query.all()
    return topic

def get_course_by_courseID(courseId):
    courses = db.session.query(Course).filter(Course.id == courseId).first()
    return courses

def get_course():
    return Course.query.all()

def get_list_course_by_topic_id(topic_id):
    # topic = db.session.query(Topic).filter(Topic.topic_name.like(username)).first()
    courses = db.session.query(Course).filter(Course.topic_id == topic_id).all()
    return courses

def get_techercourse_of_courseID(courseId):
    userTeacher = db.session.query(User.fullname).join(TeacherCourse).join(Course).filter(Course.id == courseId).all()
    return userTeacher

def get_lesson_by_ID(lessonID):
    lesson = db.session.query(Section).filter(Section.id == lessonID).first()
    return lesson

def get_all_section_by_courseID(courseId):
    sections = db.session.query(Section).filter(Course.id == courseId).all()
    return sections

def get_all_student_course_by_user_id(userID):
    courses = db.session.query(Course).join(StudentCourse).filter(StudentCourse.user_id == userID).all()
    return courses

def create_section(course_id, title, content):
    section = Section(title, content)
    course = db.session.query(Course).filter(Course.id == course_id).first()
    course.sections.append(section)
    db.session.add(section)
    db.session.commit()

def delete_section(section_id):
    section = db.session.query(Section).filter(Section.id == section_id).first()
    all_file_upload = db.session.query(FileUpload).filter(FileUpload.file_id == section_id).delete()
    db.session.delete(section)
    db.session.commit()

def update_section(section_id, title, content):
    section = db.session.query(Section).filter(Section.id == section_id).first()
    section.title = title
    section.content = content
    db.session.commit()

def get_lesson_by_course_id(course_id):
    lessons = db.session.query(Section).filter(Section.course_id == course_id).order_by(Section.id).all()
    return lessons

def get_all_teacher_course_by_user_id(userID):
    courses = db.session.query(Course).join(TeacherCourse).filter(TeacherCourse.user_id == userID).all()
    return courses

def get_all_lesson():
    return Section.query.all()

def get_file_of_lesson(lessonID):
    files = db.session.query(FileUpload).filter(FileUpload.file_id == lessonID).order_by(FileUpload.id).all()
    return files

def get_file_by_fileID(fileID):
    file = db.session.query(FileUpload).filter(FileUpload.id == fileID).first()
    return file