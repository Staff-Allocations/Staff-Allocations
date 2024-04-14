from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import get_course, get_available_staff, get_all_courses, get_all_users

allocation_views = Blueprint('allocation_views', __name__, template_folder='../templates')

@allocation_views.route('/<course_id>', methods=['GET','POST'])
def return_staff(course_id):
    courses = get_all_courses()
    staff = get_available_staff(course_id)
    return render_template('index.html', courseID=course_id, courses = courses, staff = staff)
    
