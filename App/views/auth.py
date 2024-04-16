from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from flask_login import login_required, login_user, current_user, logout_user
from.index import index_views

from App.controllers import check_username_password, login, get_user, create_user


auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


'''
Page/Action Routes
'''    
@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@auth_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_page():
    return render_template('message.html', title="Identify", message=f"You are logged in as {current_user.id} - {current_user.username}")
    

# @auth_views.route('/login', methods=['POST', 'GET'])
# def login_action():
#     if request.method == 'POST':
#         staff_id = request.form['staff_id']
#         password = request.form['password']
        

#         if check_username_password(staff_id, password):
#             return redirect('/')
#         flash('Invalid username or password given')
#         return render_template('login.html')

#     return render_template('login.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login(data['staff_id'], data['password'])
    if user:
        login_user(user)
        return 'user logged in!'
    return 'bad username or password given', 401
    

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer) 
    flash("Logged Out!")
    unset_jwt_cookies(response)
    return response

@auth_views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        email = request.form['email']
        password = request.form['password']

        user = get_user(staff_id)
        if user:
            flash('User Already Exists!')
            return render_template('signup.html')
        else:
            create_user(staff_id, password, email)

        return redirect('/')

    return render_template('signup.html')

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  response = jsonify(access_token=token) 
  set_access_cookies(response, token)
  return response

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response
