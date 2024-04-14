from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (get_all_ts, create_ts)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/addStaffDetails', methods=['GET','POST'])
def add_course_page():
    return render_template('addStaff.html')

@staff_views.route('/addStaff', methods=['GET','POST'])
def add_course():
    data = request.form
    staff_id = data['staffID']
    email = data['email']      
    email = email.lower()   #some preprocessing 
    firstName = data['firstName']
    lastName = data['lastName']
    courses = data['courses']
    courses = courses.replace(" ", "") #preprocessing
    courses = courses.upper()
    type = data['type']
    status = data['status']

    user = create_ts(staff_id, firstName, lastName, courses, email, type, status)
    if user:
        return redirect('/')
    flash ('Error occured when trying to add staff member')
    return redirect ('/')

@staff_views.route('/viewStaff', methods=['GET','POST'])
def view_staff():
    staff = get_all_ts()
    return render_template('viewStaff.html', staff = staff)

# @staff_views.route('/selectStaff', methods=['GET','POST'])
# def select_staff():
#     return render_template('selectType.html')
