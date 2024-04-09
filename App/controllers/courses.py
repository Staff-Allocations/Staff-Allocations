from App.models import Courses
from App.database import db
from App.config import config
import requests
import json

def create_course(course_id, course_name, sem_offered, type, staffAssigned, currStudents, capacity, numAssessments, totalCost):
    newCourse = Courses (course_id=course_id, course_name=course_name, sem_offered=sem_offered, type=type, staffAssigned=staffAssigned, currStudents=currStudents, capacity=capacity, numAssessments=numAssessments, totalCost=totalCost)
    db.session.add (newCourse)
    db.session.commit()
    return newCourse
  
def get_course(course_id):
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        return course
    return None

def get_all_courses():
  return Courses.query.all()

def get_students(course_id):
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        return course.currStudents
    return None

def get_staff(course_id):
    course = Courses.query.filter_by(course_id = course_id).first
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
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        return course.numAssessments
    return None

def get_total_cost(course_id):
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        return course.totalCost
    return None  
