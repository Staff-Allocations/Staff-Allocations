from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name =  db.Column(db.String(120), nullable=False)
    l_name =  db.Column(db.String(120), nullable=False)
    other_name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    type = db.Colunm (db.Integer, nullable = False) #Uses a numerical system for staff type: 0 - Lecturer, 1 - TA, 2 - Tutor, 3 - Marker, 4 - instructor
    level = db.Column(db.Integer, nullable = False) #bsc, msc, etc.
    status = db.Column(db.Integer, nullable = False)#0 - Full Time, 1 - Part time
    amountPaid = db.Column(db.Integer, nullable = False)
    coursesAssigned = db.Column(db.String(240), nullable=False)
    qualifications = db.Column(db.String(240), nullable=False)

class Instructor (Staff):
    hoursWorked = db.Column(db.Integer, nullable = True)

class Lecturer (Staff):
    hoursWorked = db.Column(db.Integer, nullable = True)

class Marker (Staff):
    scriptsMarked = db.Column(db.Integer, nullable = True)

class Tutor (Staff):
    hoursWorked = db.Column(db.Integer, nullable = True)

class TA (Staff):
    hoursWorked = db.Column(db.Integer, nullable = True)

