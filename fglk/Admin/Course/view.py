from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId
from fglk.Admin.Course.form import AddCourseForm

Admin_Course = Blueprint('Admin_Course',__name__,template_folder='templates/Admin_Course',static_folder='static')
@Admin_Course.route('/')
def ShowCourse():
      data=db.course.find()
      return render_template('Admin_ShowCourses.html',data=list(data))

@Admin_Course.route('/AddCourse',methods=['GET','POST'])
def AddCourse():
      form=AddCourseForm()
      if form.validate_on_submit():
            data={
                  'name':form.name.data
            }
            db.course.insert_one(data)
            return 'Successfully Created'
      return render_template('Admin_AddCourse.html',form=form)

       