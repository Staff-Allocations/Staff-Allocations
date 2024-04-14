from App.database import db

class Courses(db.Model):
    course_id = db.Column(db.String(120), primary_key=True)
    course_name = db.Column(db.String(120), nullable=False, unique=True)
    sem_offered = db.Column(db.Integer)
    type = db.Column(db.String(120)) 
    staffAssigned = db.Column(db.Integer, db.ForeignKey ('users.id')) #Who's currently assigned to the course
    currStudents = db.Column(db.Integer, nullable = True)
    capacity = db.Column(db.Integer, nullable = True)
    numAssessments = db.Column(db.Integer, nullable = False)
    totalCost = db.Column(db.Integer, nullable = True)

    # def getStudents(): 

    # def getStaff():

    # def addStaff(): 

    # def createCourse(): 

    # def getNumAssessments(): 

    # def numMarkersRequired(): 

    # def getTotalCost():

    
class Session(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(120), db.ForeignKey('courses.course_id')) 
    type = db.Column(db.Integer) 
    numCredits = db.Column(db.Float, nullable = False) 
    numHours = db.Column(db.Float, nullable = False) 
    numStreams = db.Column(db.Integer) 
    
