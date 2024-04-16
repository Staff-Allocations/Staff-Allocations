from flask import flash, Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for
from App.models import db
from App.controllers import calculate_total_cost, update_totalCost, calculate_cost, get_staff_type_and_status, get_type_status, delete_allocation, is_allocated, set_role, get_allocations, allocate_staff, get_course, get_available_staff, get_all_courses, calculate_lab_streams, get_staff_id_for_course_and_type, get_pay_rate_for_staff

allocation_views = Blueprint('allocation_views', __name__, template_folder='../templates')

@allocation_views.route('/<course_id>', methods=['GET','POST'])
def return_staff(course_id):
    cost=0
    cost2=0
    totalcost=0
    allocations = get_allocations(course_id)
    courses = get_all_courses()
    courses = sorted(courses, key=lambda x: x.course_name)
    staff = get_available_staff(course_id)
    rec_streams = calculate_lab_streams (course_id)
    if rec_streams is not None:
        rec_streams= int(rec_streams)
    sel_course=get_course(course_id)
    

    for allo in allocations:        #for estimated cost
        staff_ids = get_staff_id_for_course_and_type(course_id, allo.type)
        for staffID in staff_ids:
            type, status = get_staff_type_and_status(staffID)
            rate = get_pay_rate_for_staff(type, status)
            if rate is not None:
                cost += calculate_cost(rate, rec_streams)

    for allo in allocations:        #for actual cost
        staff_ids = get_staff_id_for_course_and_type(course_id, allo.type)
        for staffID in staff_ids:
            type, status = get_staff_type_and_status(staffID)
            rate = get_pay_rate_for_staff(type, status)
            if rate is not None:
                newcost= calculate_cost(rate, sel_course.numStreams)
                cost2 += newcost
                update_totalCost(course_id, cost2)

    totalcost= calculate_total_cost()
    # cost = format(cost, '.2f')
    cost2 = format(cost2, '.2f')
    totalcost= format(totalcost, '.2f')
    if staff is None:
        staff = []
        
    return render_template('index.html', courseID=course_id, totalcost=totalcost, courses = courses, staff = staff,  allocations= allocations, rec_streams=rec_streams, sel_course= sel_course, cost=cost, cost2=cost2)

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
