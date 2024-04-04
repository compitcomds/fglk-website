from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, IntegerField
from wtforms.validators import DataRequired, URL
from wtforms import  SubmitField

#faq and tags is been added seprately using js and fetch  
class AddCourseForm(FlaskForm):
    name=StringField(validators=[DataRequired()], default='')
    course_video=StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    hrs=IntegerField(validators=[DataRequired()])
    price=IntegerField(validators=[DataRequired()])
    discount=IntegerField(validators=[DataRequired()])
    img1=StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    img2=StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    img3=StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    discription=StringField(validators=[DataRequired()])
    submit=SubmitField('Submit')

class AddVideo(FlaskForm):
    title=StringField(validators=[DataRequired()])
    discription=StringField(validators=[DataRequired()])
    # link=URLField(validators=DataRequired())
    link = StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    resource=StringField( validators=[URL(message='pls link, no other kida')])
    submit=SubmitField('Submit')

class AddDocs(FlaskForm):
    title=StringField(validators=[DataRequired()])
    # discription=StringField(validators=[DataRequired()])
    # link=URLField(validators=DataRequired())
    # link = StringField('Link', validators=[DataRequired(), URL()])
    content_text=TextAreaField(validators=[DataRequired()])
    submit=SubmitField('Submit')

class AddSection(FlaskForm):
    name=StringField(validators=[DataRequired()], default='')
    submit=SubmitField('Submit')
