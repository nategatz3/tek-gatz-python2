from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddPuppyForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    age = IntegerField('Age of Puppy: ')
    submit = SubmitField('Add Puppy')

class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner: ')
    pup_id = IntegerField('Id of Puppy: ')
    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of the "Puppy":')
    submit = SubmitField('Remove Puppy')
