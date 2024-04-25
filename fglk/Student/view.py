from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId


Student = Blueprint('Student',__name__,template_folder='templates/Student',static_folder='static/Student')

@Student.before_request
@login_required
def checker():
      cookie_token = request.cookies.get('token')
      if current_user and current_user.token != cookie_token:
                logout_user()
                flash('You have been logged out due to multiple logins.', 'error')
                return redirect(url_for('Auth.login'))
      
@Student.route('/')
def studentIndex():
        return "this is std pages after login"