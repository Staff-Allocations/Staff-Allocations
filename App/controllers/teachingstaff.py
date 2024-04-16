from App.models import Users, Courses, TeachingStaff
from App.database import db
from App.config import config
import requests
import json

def create_ts(id, firstName, lastName, course_ids, email, type, status):
    newUser = TeachingStaff(id=id, firstName=firstName, lastName=lastName, email=email, type=type, status=status)
    
    for course_id in course_ids:
        course = Courses.query.get(course_id)
        if course:
            newUser.courses.append(course)

    db.session.add(newUser)
    db.session.commit()
    return newUser
  
def get_ts(id):
    staff = TeachingStaff.query.get(id)
    if (staff):
        return staff
    return None

def get_all_ts():
  return TeachingStaff.query.all()

def view_courses_assigned(id):
    user = get_user(id)
    if (user):
        return Courses.filter_by(staff_id = id)
    return None

def get_available_staff(course_id):
    staff = TeachingStaff.query.filter(TeachingStaff.courses.any(course_id=course_id)).all()

    if (staff): 
        return staff
    return None

def update_staff(id, firstName, lastName, course_ids, email, type, status):
    staff = get_ts(id)
    
    if staff:
        staff.id = int(id)
        staff.firstName = firstName
        staff.lastName = lastName
        staff.email = email
        staff.type = type
        staff.status = status

        staff.courses.clear()
        for course_id in course_ids:
            course = Courses.query.get(course_id)
            if course:
                staff.courses.append(course)

        db.session.commit()
        return staff
    return None    

def delete_staff(staff_id):
    staff = get_ts(staff_id)
    
    if staff:
        try:
            db.session.delete(staff)
            db.session.commit()
            return True  #Indicate successful deletion
        except Exception as e:
            db.session.rollback() 
            print(f"Error deleting staff: {e}")
            return False  #Indicate failure
    else:
        return False

def get_staff_type_and_status(staff_id):
    staff = TeachingStaff.query.filter_by(id=staff_id).first()

    if staff:
        return staff.type, staff.status
    else:
        return None, None
