from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId


Student = Blueprint('Student',__name__,template_folder='templates/Student',static_folder='static/Student')

@Student.before_request
@login_required
def checker():
      cookie_token = request.cookies.get('token')
      if current_user and current_user.token != cookie_token and ( current_user.role != 'Student') :
                flash('You have been logged out due to multiple logins.', 'error')
                return redirect(url_for('Auth.login'))
      elif current_user.role == 'Admin':
                return redirect(url_for('Admin.AdminIndex'))
      elif current_user.role == None:
              logout_user()
              return redirect (url_for('index'))
      
@Student.route('/')
def studentIndex():
        return f"this is sample mena {str(current_user.role)}"