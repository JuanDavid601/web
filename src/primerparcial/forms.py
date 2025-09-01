from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  DataRequired, length

class SignupForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), length(max=32)])
    title = StringField('title', validators=[DataRequired(), length(max=30)])
    description = StringField('Description', validators=[DataRequired(), length(max=250)])
    date = SubmitField('date', validators=[DataRequired(), length(max=20)])
    time = StringField('time', validators=[DataRequired(), length(max=100)])
    location = StringField('location', validators=[DataRequired(), length(max=200)])

# class PostForm(FlaskForm):
#     title = StringField('Título', validators=[DataRequired(), Length(max=128)])
#     title_slug = StringField('Título slug', validators=[Length(max=128)])
#     content = TextAreaField('Contenido')
#     submit = SubmitField('Enviar')