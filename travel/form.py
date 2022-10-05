from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, PasswordField, SubmitField, EmailField, StringField, FileField, SelectField
from wtforms.validators import InputRequired, Email, equal_to
from flask_wtf.file import FileRequired, FileField, FileAllowed
ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}


class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the
    # description meets the length requirements
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Destination Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    currency = StringField('Currency')
    submit = SubmitField("Create")


class loginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField("Login")


class registerForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    passwordConfirm = PasswordField(
        'Confrim Password', validators=[equal_to('password', "Please make sure password matches the previously entered password")])
    usertype = SelectField('User Type', choices=[(
        'guest', 'Guest'), ('admin', 'Administrator')])
    register = SubmitField("Sign up")


class commentForm(FlaskForm):
    cmt = TextAreaField("Comments:")
    submit = SubmitField("Post")
