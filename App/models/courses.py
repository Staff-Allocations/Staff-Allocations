from App.database import db

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(12), nullable=False, unique=True)
    course_name = db.Column(db.String(120), nullable=False, unique=True)
    sem_offered = db.Column(db.Integer)
    type = db.Column(db.Integer) #encodes course type to a numeric value
                                 #0 - Lecture, 1 - Lab, 2 - Tutorial
