from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId
from fglk.Admin.Course.form import AddCourseForm, AddDocs,AddVideo, AddSection

Admin_Course = Blueprint('Admin_Course',__name__,template_folder='templates/Admin_Course',static_folder='static')

# this is master route that can CURD on the course table
@Admin_Course.route('/',methods=['GET','POST'])
def Course():
      Name=request.args.get('Name')
      Delete=request.args.get('Delete', type=bool)
      if Name and Delete:
            data=db.course.find_one({'name':Name})
            db.section.delete_many({'_id': {'$in': 'sections'}})
            db.course.delete_one({'name':Name})
            return redirect(url_for('.Course'))
      if Name:
            data=db.course.find_one({'name':Name})
            if data:
                  form=AddCourseForm(**data)  
            else:
                  return redirect(url_for('.Course'))
      else:
            form=AddCourseForm()
      if form.validate_on_submit():
            data={
                  'name':form.name.data,
                  'sections':[]
            }
            if not Name:
                  db.course.insert_one(data)
            else:
                  db.course.update_one({'name':Name},{'$set':data})
            return redirect(url_for('.Course'))
      data=db.course.find()
      return render_template('Admin_Course.html',form=form,data=list(data))

# route for adding Sections in course:

@Admin_Course.route('/<string:name>',methods=['GET','POST'])
def section(name):
      Name=request.args.get('Name')
      Delete=request.args.get('Delete', type=bool)
      form=AddSection()
      if form.validate_on_submit():
            data={
                  'name':form.name.data
            }
            id=db.section.insert_one(data)
            id=id.inserted_id
            db.course.update_one({'name': name}, {'$push': {'sections': id}})
            return redirect (url_for('.section',name=name))
      data=db.section.find()
      return render_template('Admin_Section.html',form=form,data=list(data))



# type=request.args.get('Type')
#       if type=='video':
#             form=AddVideo()
#             if form.validate_on_submit():
#                   data={
#                         'title':form.title.data,
#                         'discription':form.discription.data,
#                         'link':form.link.data,
#                         'resource':form.resource.data
#                   }
#       if type == 'Docs':
#             form=AddDocs()
#             if form.validate_on_submit():
#                   data={
#                         'title':form.title.data,
#                         'discription':form.discription.data,
#                         'link':form.link.data
#                   }      
