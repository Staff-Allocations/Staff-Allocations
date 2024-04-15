from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from App.database import db

staff_course_association = Table('staff_course_association',
                                 db.Model.metadata,
                                 Column('staff_id', Integer, ForeignKey('teaching_staff.id')),
                                 Column('course_id', db.String(120), ForeignKey('courses.course_id'))
                                )

class TeachingStaff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120)) 
    email = db.Column(db.String(120), nullable=False, unique=True)
    type = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(120), nullable=False)

    courses = relationship("Courses", secondary=staff_course_association)
