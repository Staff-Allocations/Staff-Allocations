from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  email = db.Column(db.String(120), nullable = False, unique = True) 
  type = db.Column(db.Integer) #1- admin , 2- teachingstaff 3- teachingsupport, 4- adminassistant
 

  #level = db.Column(db.EmployementLevel) 
  
  # def viewCoursesAssigned(): 

  # def recommendMarker(): 

  
class TeachingSupport(db.Model):
  id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
  firstName = db.Column(db.String(120))
  lastName =db.Column(db.String(120))
  courses = db.Column(db.String(120))
  #level = db.Column(db.EmployementLevel) 
  
  # def viewCoursesAssigned(): 

class Admin(db.Model): 
  userID = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

  # def addAllocations():

  # def reviewAllocations():

  # def viewHistorical(): 
    
  # def addStaffProfile(): 

  # def updateStaff(): 

  # def confirmStaff():

  # def addCourse(): 
    
  # def updateCourses():

  # def viewBudget():

  # def projectedBudget(): 

class AdminAssistant(db.Model):
  userID = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
  
  # def addAllocations():

  # def reviewAllAllocations(): 

  # def viewHistorical(): 

