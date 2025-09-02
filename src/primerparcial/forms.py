from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import  DataRequired, length

class SignupForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), length(max=32)])
    title = StringField('title', validators=[DataRequired(), length(max=30)])
    description = StringField('description', validators=[DataRequired(), length(max=150)])
    date = DateField('date', validators=[DataRequired(), length(max=20)])
    time = TimeField('time', validators=[DataRequired(), length(max=100)])
    location = StringField('location', validators=[DataRequired(), length(max=150)])

class UsuarioForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), length(max=32)])
    Nombre = StringField('nombre', validators=[length(max=50)])
    Email = StringField('email', validators=[length(max=40)])
