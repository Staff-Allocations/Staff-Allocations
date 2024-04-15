from App.database import db

class Allocation(db.Model): 
  staffId = db.Column(db.Integer, db.ForeignKey('users.id'))
  courseId = db.Column(db.String(120), db.ForeignKey('courses.course_id')) 
  id = db.Column(db.String(120), primary_key = True)
  type = db.Column (db.String(120), db.ForeignKey('users.type')) 
  firstName = db.Column(db.String(120))
  lastName = db.Column(db.String(120))
