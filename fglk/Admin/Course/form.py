from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, URL
from wtforms import  SubmitField

class AddCourseForm(FlaskForm):
    name=StringField(validators=[DataRequired()], default='')
    submit=SubmitField('Submit')

class AddVideo(FlaskForm):
    title=StringField(validators=[DataRequired()])
    discription=StringField(validators=[DataRequired()])
    # link=URLField(validators=DataRequired())
    link = StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
    resource=StringField( validators=[DataRequired(), URL(message='pls link, no other kida')])
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
