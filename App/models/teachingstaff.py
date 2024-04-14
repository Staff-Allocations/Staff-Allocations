from App.database import db

class TeachingStaff(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstName = db.Column(db.String(120))
  lastName = db.Column(db.String(120)) 
  courses = db.Column(db.String(120))
  email = db.Column(db.String(120), nullable = False, unique = True) 
  
