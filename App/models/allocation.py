from App.database import db

class Allocation(db.Model): 
  staffId = db.Column(db.Integer, db.ForeignKey('users.id'))
  courseId = db.Column(db.String(120), db.ForeignKey('courses.course_id')) 
  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  type = db.Column (db.String(120), db.ForeignKey('users.type')) 
  # streamNum = db.Column(db.Integer) 
  # semester = db.Column(db.Integer) 
  # year = db.Column(db.Integer) 
