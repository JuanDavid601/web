from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField
from wtforms.validators import  DataRequired, Length

class SignupForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), Length(max=32)])
    title = StringField('title', validators=[DataRequired(), Length(max=30)])
    description = StringField('description', validators=[DataRequired(), Length(max=150)])
    date = DateField('date', validators=[DataRequired()])
    time = TimeField('time', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired(), Length(max=150)])

class UsuarioForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), Length(max=32)])
    nombre = StringField('nombre', validators=[Length(max=50)])
    email = StringField('email', validators=[Length(max=40)])
