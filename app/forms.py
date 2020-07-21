from flask_wtf import FlaskForm
from wtforms import (
    StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets.html5 import DateInput, TimeInput
from datetime import datetime

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

    def validate_end_date(form, field):
        start = datetime.combine(field.data, form.start_time.data)
        end = datetime.combine(field.data, form.end_time.data)
        if start >= end:
            raise ValidationError('End date/time must come after start date/time')
        elif form.start_date.data != form.end_date.data:
            raise ValidationError('Start date and end date must be same')
