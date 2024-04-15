from App.models import Courses, Allocation, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def create_course(course_id, course_name, sem_offered, type, currStudents, capacity, numAssessments, totalCost, numStreams):
    newCourse = Courses(course_id=course_id, course_name=course_name, sem_offered=sem_offered, type=type, currStudents=currStudents, capacity=capacity, numAssessments=numAssessments, numStreams=numStreams, totalCost=totalCost)
    db.session.add(newCourse)
    db.session.commit()

    return newCourse

def get_course(course_id):
    course = Courses.query.filter_by(course_id = course_id).first()
    if (course):
        return course
    return None

def get_all_courses():
  return Courses.query.all()

def get_students(course_id):
    course = Courses.query.filter_by(course_id = course_id).first()
    if (course):
        return course.currStudents
    return None

def get_staff(course_id):
    course = Courses.query.filter_by(course_id = course_id).first()
    if (course):
        return course.staffAssigned
    return None
'''
def add_Staff(course_id, staff_id)
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        staffAssigned = staffAssigned 
        return course.staffAssigned
    return None
'''
def get_num_assessment(course_id):
    course = Courses.query.filter_by(course_id = course_id).first()
    if (course):
        return course.numAssessments
    return None

def get_total_cost(course_id):
    course = Courses.query.filter_by(course_id = course_id).first()
    if (course):
        return course.totalCost
    return None  

def update_course(course_id, course_name, sem_offered, type, currStudents, capacity, numAssessments, numStreams):
    course = get_course(course_id)

    if course:
        course.course_id = course_id
        course.course_name = course_name
        course.sem_offered = sem_offered
        course.type = type
        course.currStudents = currStudents
        course.capacity = capacity
        course.numAssessments = numAssessments
        course.numStreams = numStreams
       
        db.session.commit()
        return course
    return None       

def delete_course(course_id):
    course = get_course(course_id)
    
    if course:
        try:
            db.session.delete(course)
            db.session.commit()
            return True  #Indicate successful deletion
        except Exception as e:
            db.session.rollback() 
            print(f"Error deleting course: {e}")
            return False  #Indicate failure
    else:
        return False
