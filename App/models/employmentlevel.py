from App.database import db

class EmploymnetLevel(db.Model):
  levelName = db.Column(db.String(120))
  payRate = db.Column(db.Float) 
  period = db.Column(db.Integer) 
  staffID = db.Column(db.Integer, db.ForeignKey('Users.id'))
  coursesAssigned = db.Column(db.String) 
