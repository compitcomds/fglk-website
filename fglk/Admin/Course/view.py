from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import logout_user, login_required, current_user
from fglk.database import db 
from bson.objectid import ObjectId
from fglk.Admin.Course.form import AddCourseForm, AddDocs,AddVideo, AddSection

Admin_Course = Blueprint('Admin_Course',__name__,template_folder='templates/Admin_Course',static_folder='static')

# this is master route that can CURD on the course table

@Admin_Course.route('/',methods=['GET','POST'])
def Course():
      _id=request.args.get('_id')
      Delete=request.args.get('Delete', type=bool)
      if _id and Delete:
            data=db.course.find_one({'_id':ObjectId(_id)})
            db.section.delete_many({'_id': {'$in': data['sections']}})
            db.course.delete_one({'_id':ObjectId(_id)})
            return redirect(url_for('.Course'))
      if _id:
            data=db.course.find_one({'_id':ObjectId(_id)})
            if data:
                  form=AddCourseForm(**data)  
            else:
                  return redirect(url_for('.Course'))
      else:
            form=AddCourseForm()
      if form.validate_on_submit():
            if not _id:
                  data={
                  'name':form.name.data,
                  'discription':form.discription.data,
                  'course_video':form.course_video.data,
                  'hrs':form.hrs.data,
                  'price':form.price.data,
                  'discount':form.discount.data,
                  'img1':form.img1.data,
                  'img2':form.img2.data,
                  'img3':form.img2.data,
                  'sections':[]
            }
                  db.course.insert_one(data)
            else:
                  data={
                  'name':form.name.data,
                  'discription':form.discription.data,
                  'course_video':form.course_video.data,
                  'hrs':form.hrs.data,
                  'price':form.price.data,
                  'discount':form.discount.data,
                  'img1':form.img1.data,
                  'img2':form.img2.data,
                  'img3':form.img2.data,
            }
                  db.course.update_one({'_id':ObjectId(_id)},{'$set':data})
            return redirect(url_for('.Course'))
      data=db.course.find()
      return render_template('Admin_Course.html',form=form,data=list(data))

# route for adding Sections in course:

@Admin_Course.route('/<string:course_id>',methods=['GET','POST'])
def section(course_id):
      _id=request.args.get('_id')
      Delete=request.args.get('Delete', type=bool)
      if _id and Delete:
            # data2=db.course.find_one({'name':name})
            data=db.section.find_one({'_id':ObjectId(_id)})
            # db.content.delete_many({'_id': {'$in': data2['content']}})
            db.course.update_one({'_id':ObjectId(course_id)},{'$pull':{'sections':data['_id']}})
            db.section.delete_one({'_id':ObjectId(course_id)})
            return redirect (url_for('.section',course_id=course_id))
      if _id:
            data=db.section.find_one({'_id':ObjectId(_id)})
            if data:
                  form=AddSection(**data)  
            else:
                  return redirect (url_for('.section',course_id=course_id))
      else:
            form=AddSection()
      if form.validate_on_submit():
            if not _id:
                  data={
                  'name':form.name.data,
                  'content':[]
                  }
                  inserted_section = db.section.insert_one(data)
                  section_id = inserted_section.inserted_id

                  db.course.update_one(
                  {'_id': ObjectId(course_id)},
                  {'$push': {'sections': section_id}}
                  )
            else:
                  data={
                  'name':form.name.data,
                  }
                  db.section.update_one({'_id': ObjectId(_id)}, {'$set':data})
            return redirect (url_for('.section',course_id=course_id))
      data=db.course.find_one({'_id':ObjectId(course_id)})
      data1=db.section.find({'_id':{'$in':data['sections']}})
      return render_template('Admin_Section.html',form=form,data=list(data1),course_id=course_id)

# adding content
@Admin_Course.route('/<string:course_id>/<string:section_id>',methods=['GET','POST'])
def content(course_id,section_id):
      data_type=request.args.get('data_type',type=str) #docs / video
      content_id=request.args.get('content_id')
      Delete=request.args.get('Delete', type=bool)
      # if not data_type:
      #       flash('Boskide ko kide hai','error')
      #       return redirect (url_for('.section',name=name))
      if content_id and Delete:
             deleted_content = db.content.find_one_and_delete({'_id': ObjectId(content_id)})
             content_id = deleted_content['_id']
             db.section.update_one({'_id':ObjectId(section_id)},
                                   {'$pull':{'content': content_id}})
             return redirect (url_for('.content',course_id=course_id,section_id=section_id))
      if content_id:
            data=db.content.find_one({'_id':ObjectId(content_id)})
            if data_type =='docs' and data:
                  form=AddDocs(**data)
            elif data_type == 'video' and data:
                  form=AddVideo(**data)
            else:
                  return redirect (url_for('.content',course_id=course_id,section_id=section_id))
      else:
            if data_type == 'docs':
                 form=AddDocs()
            elif data_type == 'video':
                  form=AddVideo()
            else:
                  form=False
      if  form and form.validate_on_submit() :
            if data_type == 'docs':
                  data={'type':'docs','title':form.title.data,'content_text':form.content_text.data}
            elif data_type == 'video':
                  if form.resource.data:
                        data={'title':form.title.data,'discription':form.discription.data,'link':form.link.data,'resource':form.resource.data ,'type':'video'}
                  else:
                        data={'title':form.title.data,'discription':form.discription.data,'link':form.link.data,'resource':'' ,'type':'video'}
            if not content_id:
                  inserted_content = db.content.insert_one(data)
                  content_id = inserted_content.inserted_id
                  db.section.update_one(
                  {'_id': ObjectId(section_id)},
                  {'$push': {'content': content_id}}
                  )
            else:
                  db.content.update_one({'_id': ObjectId(content_id)}, {'$set':data})
            return redirect (url_for('.content',course_id=course_id,section_id=section_id))
      data=db.section.find_one({'_id':ObjectId(section_id)})
      print(data)
      if data:
            data1=db.content.find({'_id':{'$in':data['content']}})
      else:
            data1=[]
      return render_template('Admin_Content.html',form=form,data=list(data1),course_id=course_id,section_id=section_id,data_type=data_type)


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
