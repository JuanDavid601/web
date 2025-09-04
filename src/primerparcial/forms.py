from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SelectField, IntegerField
from wtforms.validators import  DataRequired, Length, NumberRange

class SignupForm(FlaskForm):
    id = StringField('id', validators=[DataRequired(), Length(max=32)])
    title = StringField('title', validators=[DataRequired(), Length(max=30)])
    description = StringField('description', validators=[DataRequired(), Length(max=150)])
    date = DateField('date', validators=[DataRequired()])
    time = TimeField('time', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired(), Length(max=150)])
    category = SelectField('category', choices=[('deportivo','Deportivo'),
                                                ('academico','Academico'),
                                                ('cultural','Cultura')
                                                ], validators=[DataRequired()])
    Max_attendees = IntegerField('Max_attendees', validators=[DataRequired(), NumberRange(min=0, max=50, message='Numero de Asistentes')])

