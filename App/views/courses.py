from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
import string
from App.controllers import (get_course, create_course, get_all_courses)

course_views = Blueprint('courses_views', __name__, template_folder='../templates')

@course_views.route('/addCourseDetails', methods=['GET','POST'])
def add_course_page():
    return render_template('addCourse.html')

@course_views.route('/addCourse', methods=['GET','POST'])
def add_course():
    data = request.form
    course_id = data['courseID']
    course_name = data['courseName']
    course_id = course_id.replace(" ", "")
    course_id = course_id.upper()       #some preprocessing to make output neater later
    course_name = course_name.lower()
    course_name = string.capwords(course_name)
    sem_offered = data['semOffered']
    type = data['type']
    capacity = data['capacity']
    numAssessments = data['numAssessments']
    numStreams = data['numStreams']
    staffAssigned=0      #add an advanced toggle to input these
    currStudents=0
    totalCost=0
    course = create_course(course_id, course_name, sem_offered, type, staffAssigned, currStudents, capacity, numAssessments, totalCost, numStreams)
    if course:
        courses = get_all_courses()
        return redirect('/')
    flash ('Error occured when trying to add course')
    return redirect ('/')

@course_views.route('/viewCourses', methods=['GET','POST'])
def view_courses():
    courses = get_all_courses()
    return render_template('viewCourses.html', courses = courses)
