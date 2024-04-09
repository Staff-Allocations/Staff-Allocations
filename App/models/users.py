from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  email = db.Column(db.String(120), nullable = False, unique = True) 
  type = db.Column(db.Integer) #1- admin , 2- teachingstaff 3- teachingsupport, 4- adminassistant
 
class TeachingStaff(db.Model):
  id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
  firstName = db.Column(db.String(120))
  lastName =db.Column(db.String(120)) 
  #level = db.Column(db.EmployementLevel) 
  
  # def viewCoursesAssigned(): 

  # def recommendMarker(): 

  
class TeachingSupport(db.Model):
  id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
  firstName = db.Column(db.String(120))
  lastName =db.Column(db.String(120)) 
  #level = db.Column(db.EmployementLevel) 
  
  # def viewCoursesAssigned(): 

class Admin(db.Model): 
  id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
  userID = db.Column(db.Integer, db.ForeignKey('Users.id'))

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
  id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
  userID = db.Column(db.Integer, db.ForeignKey('Users.id'))
  
  # def addAllocations():

  # def reviewAllAllocations(): 

  # def viewHistorical(): 

