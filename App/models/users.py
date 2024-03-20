from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  firstName = db.Column(db.String(120), nullable = False) 
  lastName = db.Column(db.String(120), nullable = False) 
  otherName = db.Column(db.String(120), nullable = True) 
  email = db.Column(db.String(120), nullable = False, unique = True) 
  level = db.Column(db.Integer) #1- MSc, 2- PhD, etc --determine scale 
  type = db.Column(db.Integer) #1- admin , 2- teachingstaff 3- teachingsupport, 4- adminassistant
  amountPaid = db.Column(db.Float, nullable = False) 

class TeachingStaff(db.Model): 
  staff_id = db.Column(db.Integer, primary_key = True) 
  role = db.Column(db.String(120) ) 
  qualifications = db.Column(db.String(120)) #areas they specialise in
  coursesAssigned = db.Column(db.String(120)) 

  def viewCoursesAssigned(): 

  def recommendMarker(): 

 #def checkHoursWorked():
  
class TeachingSupport(db.Model):
  staff_id = db.Column(db.Integer, primary_key= True)
  role = db.Column(db.String(120)) 
  qualifications = db.Column(db.String(120)) #areas they specialise in
  coursesAssigned = db.Column(db.String(120)) 

  def viewCoursesAssigned(): 

class Admin(db.Model): 
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(120)) 

  def addStaffProfile(): 

  def editStaff(): 

  def confirmStaff():

  def updateCourses():

  def reviewAllAllocations():

  def viewBudget():

class AdminAssistand(db.Model): 
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(120)) 

  def addAllocations():

  def reviewAllAllocations(): 

  def viewHistorical(): 

class Instructor (Staff):
  def recommendMarker(): 

  def viewAllocations(): 
   
class Lecturer (Staff):
  def recommendMarker(): 

  def viewAllocations(): 
   
class Marker (Staff):
  scriptsMarked = db.Column(db.Integer, nullable = True)

  def getAssignedCourses(): 

  def getNumScripts():

  def generateClaimForm():

class Tutor (Staff):
  hoursWorked = db.Column(db.Integer, nullable = True)

  def generateClaimForm(): 
    
  def checkHoursWorked():

  def checkClaims(): 

class TA (Staff):
  hoursWorked = db.Column(db.Integer, nullable = True)

  def checkHoursWorked():  
