from flask import flash, Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for
from App.models import db
from App.controllers import delete_allocation, is_allocated, set_role, get_allocations, allocate_staff, get_course, get_available_staff, get_all_courses

allocation_views = Blueprint('allocation_views', __name__, template_folder='../templates')

@allocation_views.route('/<course_id>', methods=['GET','POST'])
def return_staff(course_id):
    allocations = get_allocations(course_id)
    courses = get_all_courses()
    staff = get_available_staff(course_id)
    if staff is None:
        staff = []
    return render_template('index.html', courseID=course_id, courses = courses, staff = staff,  allocations= allocations )

@allocation_views.route('/<course_id>/<staff_id>/<role>/<fname>/<lname>', methods = ['GET','POST'])
def allocateStaff(course_id, staff_id, role, fname, lname):
    id = str(course_id) + str(staff_id)
    allocated = is_allocated(id)
    courses = get_all_courses()
    staff = get_available_staff(course_id)
    allocations = get_allocations(course_id)
    if allocated:
        flash ('User already Allocated!')
        return redirect (url_for('allocation_views.return_staff', course_id=course_id))

    allocate = allocate_staff(id, course_id, staff_id, role, fname, lname)
    allocations = get_allocations(course_id)
    flash ('User allocated successfully!')
    return redirect (url_for('allocation_views.return_staff', course_id=course_id))

@allocation_views.route('/delete_allocation_routes/<id>/<course_id>', methods=['GET', 'POST'])
def delete_staff_route(id, course_id):
    deleted = delete_allocation(id)
    if deleted:
        flash('Successfully deleted')
        return redirect (url_for('allocation_views.return_staff', course_id=course_id))
    else: 
        flash('Error in deleting allocation')
        return redirect (url_for('allocation_views.return_staff', course_id=course_id))
