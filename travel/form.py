from email.message import EmailMessage
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, PasswordField, SubmitField, EmailField, StringField, FileField
from wtforms.validators import InputRequired, Length, equal_to


class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the
    # description meets the length requirements
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Cover Image')
    currency = StringField('Currency')
    submit = SubmitField("Create")


class loginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField("Login")


class registerForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email')
    password = PasswordField('Password', validators=[InputRequired()])
    passwordConfirm = PasswordField(
        'Confrim Password', validators=[equal_to('password', "Please make sure password matches the previously entered password")])
    register = SubmitField("Sign up")


class commentForm(FlaskForm):
    cmt = TextAreaField("Comments:")
    submit = SubmitField("Post")
