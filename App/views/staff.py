from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (get_staff, create_User)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/addStaffDetails', methods=['GET','POST'])
def add_course_page():
    return render_template('addStaff.html')

@staff_views.route('/addStaff', methods=['GET','POST'])
def add_course():
    data = request.form
    staff_id = data['staffID']
    email = data['email']      
    email = email.lower()   #some preprocessing to make output neater later
    type = data['type']
    
    user = create_User(id, email, type)
    if user:
        return redirect('/')
    flash ('Error occured when trying to add staff member')
    return redirect ('/')
