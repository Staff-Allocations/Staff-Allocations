from App.models import Users
from App.database import db
from App.config import config
import requests
import json

def create_User(id, firstname, lastname, othername, email, level, type, amountPaid):
    newUser = Users (id=id, firstname=firstname, lastname=lastname, othername=othername, email=email, level=level, type=type, amountPaid=amountPaid)
    db.session.add (newUser)
    db.session.commit()
    return newUser
  
def get_user(firstname):
    user = Users.query.filter_by(firstname = firstname).first
    if (user):
        return user
    return None

def get_all_users():
  return Users.query.all()
