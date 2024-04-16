from App.models import Courses, Allocation, TeachingStaff
from App.database import db
from App.config import config
import requests
import json
import math

def create_course(course_id, course_name, sem_offered, type, lab_size, currStudents, capacity, numAssessments, totalCost, numStreams):
    newCourse = Courses(course_id=course_id, course_name=course_name, sem_offered=sem_offered, type=type, lab_size=lab_size, currStudents=currStudents, capacity=capacity, numAssessments=numAssessments, numStreams=numStreams, totalCost=totalCost)
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

def get_course_capacity(course_id):
    course = Courses.query.filter_by(course_id=course_id).first()
    if course:
        return course.capacity
    else:
        return None

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

def update_course(course_id, course_name, sem_offered, type, lab_size, currStudents, capacity, numAssessments, numStreams):
    course = get_course(course_id)

    if course:
        course.course_id = course_id
        course.course_name = course_name
        course.sem_offered = sem_offered
        course.type = type
        course.lab_size=lab_size
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

def calculate_lab_streams(course_id):
    course = get_course(course_id)

    if course:
        rec_streams = math.ceil(course.capacity/course.lab_size)
        
        return rec_streams
    return None

def update_numStreams(course_id, numStreams):
    course = get_course(course_id)

    if course:
        course.numStreams = numStreams
       
        db.session.commit()
        return course
    return None   

def update_totalCost(course_id, cost):
    course=get_course(course_id)
    
    if course:
        course.totalCost=cost
        db.session.commit()
        return course
    return None  
    
def calculate_total_cost():
    total_cost = 0
    courses = Courses.query.all()
    for course in courses:
        if course.totalCost is not None:
            total_cost += course.totalCost
    return total_cost
