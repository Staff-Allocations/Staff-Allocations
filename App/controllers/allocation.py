from App.models import Courses, Allocation, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def allocate_staff(course_id, staff_id):
    newAllo = Allocation (staffId=staff_id, courseId=course_id)  
    db.session.add (newAllo)
    db.session.commit()
    return newAllo

def get_allocations():
    return Allocation.query.all()
