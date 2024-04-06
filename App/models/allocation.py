from App.database import db

class Allocation(db.Model):
  staffId = db.Column(db.Integer, db.ForeignKey('Users.id')) 
  courseId = db.Column(db.String(120), db.ForeignKey('Courses.course_id') 
  streamNum = db.Column(db.Integer) 
  semester = db.Column(db.Integer) 
  year = db.Column(db.Integer) 

  def getStaffAssigned(): 
