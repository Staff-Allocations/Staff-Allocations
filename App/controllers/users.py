from App.models import Users, Courses
from App.database import db
from App.config import config
import requests
import json

def create_User(id, firstname, lastname, othername, email, level, type, amountPaid):
    newUser = Users (id=id, firstname=firstname, lastname=lastname, othername=othername, email=email, level=level, type=type, amountPaid=amountPaid)
    db.session.add (newUser)
    db.session.commit()
    return newUser
  
def get_user(id):
    user = Users.query.filter_by(id = id).first
    if (user):
        return user
    return None

def get_all_users():
  return Users.query.all()

def view_courses_assigned(id):
    user = get_user(id)
    if (user):
        return Courses.filter_by(staff_id = id)
    return None
    
        
    
    
