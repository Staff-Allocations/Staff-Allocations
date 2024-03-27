from App.models import Courses
from App.database import db
from App.config import config
import requests
import json

def create_Course(course_id, course_name, sem_offered, type, staffAssigned, currStudents, capacity, numAssessments, totalCost):
    newCourse = Users (course_id=course_id, course_name=course_name, sem_offered=sem_offered, type=type, staffAssigned=staffAssigned, currStudents=currStudents, capacity=capacity, numAssessments=numAssessments, totalCost=totalCost)
    db.session.add (newCourse)
    db.session.commit()
    return newCourse
  
def get_user(course_id):
    course = Courses.query.filter_by(course_id = course_id).first
    if (course):
        return course
    return None

def get_all_Courses():
  return Courses.query.all()
