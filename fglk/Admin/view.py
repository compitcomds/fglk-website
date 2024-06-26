from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId


Admin = Blueprint('Admin',__name__,template_folder='templates/Admin',static_folder='static')

@Admin.before_request
@login_required
def checker():
      cookie_token = request.cookies.get('token')
      if current_user and current_user.token != cookie_token:
                logout_user()
                flash('You have been logged out due to multiple logins.', 'error')
                return redirect(url_for('Auth.login'))


@Admin.route('/')
def AdminIndex():
      print(current_user.token,"this is current user token")
      print(request.cookies.get('token'),"this is request user token")
      return "this is admin"

from .Course.view import Admin_Course
Admin.register_blueprint(Admin_Course,url_prefix='/course')

