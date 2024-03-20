from App.database import db

class Courses(db.Model):
    course_id = db.Column(db.String(120), primary_key=True)
    course_name = db.Column(db.String(120), nullable=False, unique=True)
    sem_offered = db.Column(db.Integer)
    type = db.Column(db.Integer) #encodes course type to a numeric value: 1 - Lab, 2 - Tutorial
    staffAssigned = db.Column(db.Integer, nullable = True) #Who's currently assigned to the course
    currStudents = db.Column(db.Integer, nullable = True)
    capacity = db.Column(db.Integer, nullable = True)
    numAssessments = = db.Column(db.Integer, nullable = True)
    totalCost = = db.Column(db.Integer, nullable = True)  


    
class Session(db.Model):
    course_id = db.Column(db.String(120), db.ForeignKey('Courses.course_id')) 
    type = db.Column(db.Integer) 
    numCredits = db.Column(db.Float, nullable = False) 
    numHours = db.Column(db.Float, nullable = False) 
    numStreams = db.Column(db.Integer) 
    
