from flask_wtf import FlaskForm
from wtforms import (
    StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import DateInput, TimeInput

class AppointmentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[
                        DataRequired()], widget=DateInput())
    start_time = TimeField('start_time', validators=[
                        DataRequired()], widget=TimeInput())
    end_date = DateField('end_date', validators=[
                         DataRequired()], widget=DateInput())
    end_time = TimeField('end_time', validators=[
                         DataRequired()], widget=TimeInput())
    description = TextAreaField('description', validators=[DataRequired()])
    private = BooleanField('private')
    submit = SubmitField('Save')
