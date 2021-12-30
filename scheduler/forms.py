from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class RunModel(FlaskForm):
    num_gps = IntegerField('Number of GPs', validators=[DataRequired(), NumberRange(min=1, max=None, message='stop')])
    num_slots = IntegerField('Number of timeslots', validators=[DataRequired(), NumberRange(min=1, max=20, message='stop1')])
    num_to_book = IntegerField('Number of slots to book', validators=[DataRequired(), NumberRange(min=1, max=None, message='stop2')])
    num_prebooked = IntegerField('Number of slots prebooked', validators=[DataRequired(), NumberRange(min=1, max=None, message='stop3')])
    run = SubmitField('Run')