from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name =  db.Column(db.String, nullable=False)
    l_name =  db.Column(db.String, nullable=False)
    other_name = db.Column(db.String, nullable=True)
    staff_type = db.Colunm (db.Integer, nullable = False) #Uses a numerical system for staff type
                                                          #0 - Lecturer, 1 - TA, 2 - Tutor, 3 - Marker
