from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId


Admin = Blueprint('Admin',__name__,template_folder='templates/Admin',static_folder='static/admin')

@Admin.before_request
@login_required
def checker():
      cookie_token = request.cookies.get('token')
      if current_user and current_user.token != cookie_token and ( str(current_user.role) != 'Admin') :
                flash('You have been logged out due to multiple logins.', 'error')
                return redirect(url_for('Auth.login'))
      elif current_user.role == "Student":
             flash('u are not an admin ')
             return redirect (url_for("Student.studentIndex"))
      elif current_user.role == None:
              logout_user()
              return redirect (url_for('index'))

@Admin.route('/')
def AdminIndex():   
      print(current_user.token,"this is current user token")
      print(request.cookies.get('token'),"this is request user token")
      return render_template('index_admin.html')

from .Course.view import Admin_Course
Admin.register_blueprint(Admin_Course,url_prefix='/course')

from .Community.view import Admin_Community
Admin.register_blueprint(Admin_Community,url_prefix='/community')