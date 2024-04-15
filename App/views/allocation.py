from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for
from App.models import db
from App.controllers import set_role, get_allocations, allocate_staff, get_course, get_available_staff, get_all_courses

allocation_views = Blueprint('allocation_views', __name__, template_folder='../templates')

@allocation_views.route('/<course_id>', methods=['GET','POST'])
def return_staff(course_id):
    allocations = get_allocations()
    courses = get_all_courses()
    staff = get_available_staff(course_id)
    return render_template('index.html', courseID=course_id, courses = courses, staff = staff,  allocations= allocations )

@allocation_views.route('/<course_id>/<staff_id>', methods = ['GET','POST'])
def allocateStaff(course_id, staff_id):
    role =set_role(staff_id)
    allocate = allocate_staff(course_id, staff_id, role)
    allocations = get_allocations()
    staff = get_available_staff(course_id)
    courses = get_all_courses()
    return redirect ('/')

    
