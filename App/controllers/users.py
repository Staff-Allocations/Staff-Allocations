from App.models import Users, Courses, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def create_ts(id, firstName, lastName, courses, email):
    newUser = TeachingStaff (id=id, firstName=firstName, lastName=lastName, courses=courses, email=email)
    db.session.add (newUser)
    db.session.commit()
    return newUser
  
def get_ts(id):
    user = TeachingStaff.query.filter_by(id = id).first
    if (user):
        return user
    return None

def get_all_ts():
  return TeachingStaff.query.all()

def view_courses_assigned(id):
    user = get_user(id)
    if (user):
        return Courses.filter_by(staff_id = id)
    return None

def get_available_staff(course_id):
    staff = TeachingStaff.query.filter_by(courses=course_id)
    if (staff): 
        return staff
    return None
