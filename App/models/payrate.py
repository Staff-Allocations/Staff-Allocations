from App.database import db

class PayRate(db.Model): 
  id = db.Column(db.String(120), primary_key=True)
  staff_type = db.Column(db.String(120)) 
  status = db.Column (db.String(120))
  pay = db.Column(db.String(120))
