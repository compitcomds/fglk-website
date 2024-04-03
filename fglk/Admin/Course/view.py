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
            db.section.delete_many({'_id': {'$in': data['sections']}})
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
      if Name and Delete:
            # data2=db.course.find_one({'name':name})
            data=db.section.find_one({'name':Name})
            # db.content.delete_many({'_id': {'$in': data2['content']}})
            db.course.update_one({'name':name},{'$pull':{'sections':data['_id']}})
            db.section.delete_one({'name':Name})
            return redirect (url_for('.section',name=name))
      if Name:
            data=db.section.find_one({'name':Name})
            if data:
                  form=AddSection(**data)  
            else:
                  return redirect (url_for('.section',name=name))
      else:
            form=AddSection()
      if form.validate_on_submit():
            data={
                  'name':form.name.data,
                  'content':[]
            }
            if not Name:
                  inserted_section = db.section.insert_one(data)
                  section_id = inserted_section.inserted_id

                  db.course.update_one(
                  {'name': name},
                  {'$push': {'sections': section_id}}
                  )
            else:
                  db.section.update_one({'name': Name}, {'$set':data})
            return redirect (url_for('.section',name=name))
      data=db.course.find_one({'name':name})
      data1=db.section.find({'_id':{'$in':data['sections']}})
      return render_template('Admin_Section.html',form=form,data=list(data1),name=name)


@Admin_Course.route('/<string:name>/<string:section>',methods=['GET','POST'])
def content(name,section):
      data_type=request.args.get('data_type',type=str) #docs / video
      Name=request.args.get('Name')
      Delete=request.args.get('Delete', type=bool)
      if not data_type:
            flash('Boskide ko kide hai','error')
            return redirect (url_for('.section',name=name))
      if Name and Delete:
            return redirect (url_for('.content',name=name,section=section))
      if Name:
            data=db.content.find_one({'name':Name})
            if data_type =='docs' and data:
                  form=AddDocs(**data)
            elif data_type == 'video' and data:
                  form=AddVideo(**data)
            else:
                  return redirect (url_for('.content',name=name,section=section))
      else:
            if data_type == 'docs':
                 form=AddDocs()
            if data_type == 'video':
                  form=AddVideo()
      if form.validate_on_submit():
            if data_type == 'docs':
                  data={'type':'docs','title':form.title.data,'content_text':form.content_text.data}
            elif data_type == 'video':
                  data={'title':form.title.data,'discription':form.discription.data,'link':form.link.data,'resource':form.resource.data}
            if not Name:
                  inserted_content = db.content.insert_one(data)
                  content_id = inserted_content.inserted_id
                  db.section.update_one(
                  {'name': section},
                  {'$push': {'content': content_id}}
                  )
            else:
                  db.section.update_one({'name': Name}, {'$set':data})
            return redirect (url_for('.content',name=name,section=section))
      data=db.section.find_one({'name':name})
      if data:
            data1=db.content.find({'_id':{'$in':data['content']}})
      else:
            data1=[]
      return render_template('Admin_Content.html',form=form,data=list(data1),name=name,section=section,data_type=data_type)


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
