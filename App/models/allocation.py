from App.database import db

class Allocation(db.Model):
  staffId = db.Column(db.Integer, db.ForeignKey('Staff.staff_id')
  courseId = db.Column(db.String(120), db.ForeignKey('Courses.course_id') 
