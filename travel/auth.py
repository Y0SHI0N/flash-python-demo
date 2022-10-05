from flask import Blueprint, render_template, redirect, url_for, flash, request
from .form import loginForm, registerForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from . import db

# create a blueprint
bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    logInForm = loginForm()
    error = None
    if (logInForm.validate_on_submit()):
        user_name = logInForm.username.data
        password = logInForm.password.data
        u1 = User.query.filter_by(name=user_name).first()

    # if there is no user with that name
        if u1 is None:
            error = 'Incorrect user name'
    # check the password - notice password hash function
    # takes the hash and password
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            # all good, set the login_user
            login_user(u1)
            print('Successfully logged in')
            flash('You logged in successfully')
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)
            return redirect(url_for('auth.login'))
    return render_template('user.html', form=logInForm,  heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    regForm = registerForm()
    if regForm.validate_on_submit():
        # get username, password and email from the form
        uname = regForm.username.data
        pwd = regForm.password.data
        email = regForm.email.data
        utype = regForm.usertype.data

        pwd_hash = generate_password_hash(pwd)
        # create a new user model object
        new_user = User(name=uname, password_hash=pwd_hash,
                        emailid=email, usertype=utype)
        db.session.add(new_user)
        db.session.commit()
        flash("Registered user successfully")
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=regForm,  heading='Register')


@bp.route('/logout')
def logout():
    logout_user()
    return 'Successfully logged out user'
