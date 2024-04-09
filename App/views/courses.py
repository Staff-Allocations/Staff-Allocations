from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for

from App.controllers import (get_course)

course_views = Blueprint('courses_views', __name__, template_folder='../templates')
