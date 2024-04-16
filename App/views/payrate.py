from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from App.controllers import get_all_rates, create_payrate, get_payrate, update_payrate


payrate_views= Blueprint('payrate_views', __name__, template_folder='../templates')

@payrate_views.route ('/viewpayrates', methods=['GET','POST'])
def view_rates():
    rates = get_all_rates()

    return render_template('viewPay.html', rates=rates)


@payrate_views.route ('/addpayrates', methods=['GET','POST'])
def add_rates_page():
     return render_template('addPay.html')


@payrate_views.route ('/addpay', methods=['GET','POST'])
def add_rates():
    staff_type = request.form.get('staffType')
    status = request.form.get('status')
    pay = request.form.get('payRate')
    status_for_id= status.replace(" ", "")
    id = str(staff_type) + str(status_for_id)
    payrate = get_payrate(id)
    
    if payrate:
        flash ('Payrate already Exists!')
    else:
        flash ('Payrate added')
        payrate = create_payrate (id, staff_type, status, pay)
    return redirect(url_for('payrate_views.view_rates'))

@payrate_views.route ('/updatepay/<id>', methods=['GET','POST'])
def update_rates(id):
    rate= get_payrate(id)

    if request.method == 'POST':
        # staff_type = request.form['staffType']
        # status = request.form['status']
        pay = request.form.get('payRate')

        rate = update_payrate (id, pay)

        return redirect (url_for('payrate_views.view_rates'))
    
    return render_template('updatePay.html', rate=rate)
