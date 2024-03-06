from App.database import db

class Historical(db.Model):
  staffId = db.Column(db.Integer, db.ForeignKey('Staff.id'))
  courseId= db.Column(db.Integer, db.ForeignKey('Courses.id'))
  yearTaught= db.Column(db.Integer, nullable = True)
  passRate = db.Column(db.Integer, nullable = True)
  
