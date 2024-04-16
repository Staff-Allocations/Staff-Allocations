from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
import string
from App.controllers import (update_numStreams, delete_course, get_course, update_course, create_course, get_all_courses)

course_views = Blueprint('courses_views', __name__, template_folder='../templates')

@course_views.route('/addCourseDetails', methods=['GET','POST'])
def add_course_page():
    return render_template('addCourse.html')

@course_views.route('/addCourse', methods=['GET','POST'])
def add_course():
    data = request.form
    course_id = data['courseID']
    course_name = data['courseName']
    course_id = course_id.replace(" ", "")  #some preprocessing 
    course_id = course_id.upper()       
    course_name = course_name.lower()
    course_name = string.capwords(course_name)
    sem_offered = data['semOffered']
    type = data['type']
    capacity = data['capacity']
    numAssessments = data['numAssessments']
    lab_size = request.form['lab_size']
    numStreams = data['numStreams']
    currStudents=0
    totalCost=0
    course = create_course(course_id, course_name, sem_offered, type, lab_size, currStudents, capacity, totalCost, numAssessments, numStreams)
    
    if course:
        courses = get_all_courses()
        return redirect('/')
    flash ('Error occured when trying to add course')
    return redirect ('/')

@course_views.route('/viewCourses', methods=['GET','POST'])
def view_courses():
    courses = get_all_courses()
    return render_template('viewCourses.html', courses = courses)

@course_views.route('/update_course/<course_id>', methods=['GET', 'POST'])
def update_course_view(course_id):
    course = get_course(course_id)

    if request.method == 'POST':
        course_name = request.form['course_name']
        sem_offered = request.form['sem_offered']
        type = request.form['type']
        currStudents = request.form['currStudents']
        capacity = request.form['capacity']
        numAssessments = request.form['numAssessments']
        lab_size = request.form['lab_size']
        numStreams = request.form['numStreams']
        
        course_id = course_id.replace(" ", "")  #some preprocessing 
        course_id = course_id.upper()       
        course_name = course_name.lower()
        course_name = string.capwords(course_name)

        course = update_course(course_id, course_name, sem_offered, type, lab_size, currStudents, capacity, numAssessments, numStreams)

        return redirect(url_for('courses_views.view_courses'))

    return render_template('updateCourses.html', course=course)

@course_views.route('/delete_course_routes/<course_id>', methods=['POST'])
def delete_course_route(course_id):
    deleted = delete_course(course_id)
    if deleted:
        flash('Successfully deleted ', course_id)
        return redirect(url_for('courses_views.view_courses'))
    else: 
        flash('Error in deleting course')
        return redirect(url_for('courses_views.view_courses'))
    
@course_views.route('/editNumStream/<course_id>', methods=['POST'])
def update_num_streams(course_id):
    numStreams = request.form['current_streams']
    course = update_numStreams(course_id, numStreams)

    return redirect (url_for('allocation_views.return_staff', course_id=course_id))
