from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from App.database import db


course_staff_association = Table('course_staff_association',
                                 db.Model.metadata,
                                 Column('course_id', db.String(120), ForeignKey('courses.course_id')),
                                 Column('user_id', Integer, ForeignKey('users.id'))
                                )

class Courses(db.Model):
    course_id = db.Column(db.String(120), primary_key=True)
    course_name = db.Column(db.String(120), nullable=False, unique=True)
    sem_offered = db.Column(db.Integer)
    type = db.Column(db.String(120)) 
    lab_size = db.Column(db.Integer)
    staffAssigned = relationship("Users", secondary=course_staff_association)
    currStudents = db.Column(db.Integer, nullable=True)
    capacity = db.Column(db.Integer, nullable=True)
    numAssessments = db.Column(db.Integer, nullable=False) 
    numStreams = db.Column(db.Integer)
    totalCost = db.Column(db.Integer, nullable = True)


    
# class Session(db.Model):
#     sid = db.Column(db.Integer, primary_key=True)
#     course_id = db.Column(db.String(120), db.ForeignKey('courses.course_id')) 
#     type = db.Column(db.Integer) 
#     numCredits = db.Column(db.Float, nullable = False) 
#     numHours = db.Column(db.Float, nullable = False) 
#     numStreams = db.Column(db.Integer) 
