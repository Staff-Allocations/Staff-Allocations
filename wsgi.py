import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import (create_user, get_all_users_json, get_all_users, create_course, get_all_courses)

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


course_cli = AppGroup('course', help='course object commands') 

@course_cli.command("create", help="Creates a course")
@click.argument("course_id")
@click.argument("course_name")
@click.argument("sem_offered")
@click.argument("type")
def create_course_command(course_id, course_name, sem_offered, type):
    staffAssigned = 0
    currStudents =0
    numAssessments = 1 
    capacity = 200
    totalCost = 0
    create_course(course_id, course_name, sem_offered, type, staffAssigned, currStudents, capacity, numAssessments, totalCost)
    print(f'{course_id} created!')

@course_cli.command("list", help="Lists courses in the database")
@click.argument("format", default="string")
def list_user_command(format):
    print(get_all_courses())


app.cli.add_command(course_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
