from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (get_course, create_course, get_all_courses)

course_views = Blueprint('courses_views', __name__, template_folder='../templates')

@course_views.route('/addCourseDetails', methods=['GET','POST'])
def add_course_page():
    return render_template('addCourse.html')

@course_views.route('/addCourse', methods=['GET','POST'])
def add_course():
    data = request.form
    course_id = data['courseID']
    course_id = course_id.replace(" ", "")
    course_id = course_id.upper()
    course_name = data['courseName']
    sem_offered = data['semOffered']
    type = data['type']
    staffAssigned=0      #add an advanced toggle to input these
    currStudents=0
    capacity=200
    numAssessments=1
    totalCost=0
    course = create_course(course_id, course_name, sem_offered, type, staffAssigned, currStudents, capacity, numAssessments, totalCost)
    if course:
        courses = get_all_courses()
        return render_template('index.html', courses=courses)
    flash ('Error occured when trying to add course')
    return redirect ('/')
