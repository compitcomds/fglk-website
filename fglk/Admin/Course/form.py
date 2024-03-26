from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField,RadioField
from wtforms.validators import DataRequired
from wtforms import  SubmitField

class AddCourseForm(FlaskForm):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField('Submit')