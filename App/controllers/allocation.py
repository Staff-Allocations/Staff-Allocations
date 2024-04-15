from App.models import Courses, Allocation, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def allocate_staff(course_id, staff_id, type):
    if ((Allocation.query.filter_by(staffId = staff_id).first == None) and (Allocation.query.filter_by(courseId = course_id).first == None)):
        newAllo = Allocation (staffId=staff_id, courseId=course_id, type = type)  
        db.session.add (newAllo)
        db.session.commit()
        return newAllo
    return None

def get_allocations():
    return Allocation.query.all()

def set_role(staff_id):
    user = TeachingStaff.query.filter_by(id = staff_id).first
    if (user):
        return user
    
