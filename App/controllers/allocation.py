from App.models import Courses, Allocation, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def allocate_staff(id, course_id, staff_id, type, firstName, lastName):
    newAllo = Allocation (id=id, staffId=staff_id, courseId=course_id, type=type, firstName=firstName, lastName=lastName)  
    db.session.add (newAllo)
    db.session.commit()
    return newAllo
    return None

def get_allocations(course_id):
    return Allocation.query.filter_by(courseId=course_id)

def is_allocated(Id):
    allocated= Allocation.query.filter_by(id=Id).first()
    return allocated

def set_role(staff_id):
    user = TeachingStaff.query.filter_by(id = staff_id).first()
    if (user):
        return user
