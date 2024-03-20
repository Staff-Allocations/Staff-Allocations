from App.database import db

class Assessment(db.Model):
  assessmentType = db.Column(db.Integer)
  courseCode = db.Column(db.String(120), db.ForeignKey('Courses.course_id')
  rate = db.Column(db.Float)
  name = db.Column(db.String(120)) 
