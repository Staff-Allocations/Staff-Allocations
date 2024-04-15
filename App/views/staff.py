from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
import string
from App.controllers import (get_courses_for_staff, get_all_courses, delete_staff, get_all_ts, create_ts, update_staff, get_ts)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/addStaffDetails', methods=['GET','POST'])
def add_course_page():
    courses = get_all_courses()
    return render_template('addStaff.html', courses=courses)

@staff_views.route('/addStaff', methods=['GET','POST'])
def add_staff():
    data = request.form
    staff_id = data['staffID']
    email = data['email']      
    firstName = data['firstName']
    lastName = data['lastName']
    courses = request.form.getlist('courses')
    type = data['type']
    status = data['status']

    firstName = firstName.lower()   #preprocessing
    firstName = string.capwords(firstName)
    lastName = lastName.lower()
    lastName = string.capwords(lastName)
    email = email.lower()

    user = create_ts(staff_id, firstName, lastName, courses, email, type, status)
    if user:
        return redirect('/')
    flash ('Error occured when trying to add staff member')
    return redirect ('/')

@staff_views.route('/viewStaff', methods=['GET','POST'])
def view_staff():
    staff = get_all_ts()
    # allocations = get_courses_for_staff()
    return render_template('viewStaff.html', staff = staff)

@staff_views.route('/update_staff/<staff_id>', methods=['GET', 'POST'])
def update_staff_view(staff_id):
    staff = get_ts(staff_id)
    courses=get_all_courses()
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        if 'courses' in request.form:
            courses = request.form.getlist('courses')
        else:
            courses = []
        email = request.form['email']
        type = request.form['type']
        status = request.form['status']
        
        firstName = firstName.lower()   #preprocessing
        firstName = string.capwords(firstName)
        lastName = lastName.lower()
        lastName = string.capwords(lastName)
        email = email.lower()

        staff = update_staff(staff_id, firstName, lastName, courses, email, type, status)

        return redirect(url_for('staff_views.view_staff'))

    return render_template('updateStaff.html', staff=staff, courses=courses)

@staff_views.route('/delete_staff_routes/<staff_id>', methods=['POST'])
def delete_staff_route(staff_id):
    deleted = delete_staff(staff_id)
    if deleted:
        flash('Successfully deleted ', staff_id)
        return redirect(url_for('staff_views.view_staff'))
    else: 
        flash('Error in deleting course')
        return redirect(url_for('staff_views.view_staff'))
