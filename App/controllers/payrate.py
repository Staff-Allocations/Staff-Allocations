from App.models import PayRate, TeachingStaff, Allocation
from App.database import db
from App.config import config

def create_payrate(id, staff_type, status, pay):
    newPay = PayRate(id=id, staff_type=staff_type, status=status, pay=pay)
    db.session.add(newPay)
    db.session.commit()

    return newPay

def get_payrate(id):
    payrate = PayRate.query.filter_by(id = id).first()
    if (payrate):
        return payrate
    return None

def update_payrate(id, pay):
    payrate =get_payrate(id)

    if payrate:
        # payrate.staff_type=staff_type
        # payrate.status=status
        payrate.pay=pay
        db.session.commit()

        return payrate
    return None  

def get_pay_rate_for_staff(staff_type, status):
    payrate = PayRate.query.filter_by(staff_type=staff_type, status=status).first()

    if payrate:
        return payrate.pay
    return None

def get_all_rates():
    all_pay_rates = PayRate.query.all()

    return all_pay_rates

def calculate_cost(rate, num_streams):
    return float(float(rate) * float(num_streams))

def get_type_status(staff_type,status):
    pay_rate = PayRate.query.filter_by(staff_type=staff_type, status=status).first()
    if pay_rate:
        return pay_rate
    return None
