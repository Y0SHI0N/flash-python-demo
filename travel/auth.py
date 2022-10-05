from flask import Blueprint, render_template, request, redirect, url_for, flash
from .form import loginForm, registerForm

# create a blueprint
bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    logInForm = loginForm()
    if logInForm.validate_on_submit():
        print('Successfully logged in')
        flash('You logged in successfully')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=logInForm,  heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    regForm = registerForm()
    if regForm.validate_on_submit():
        print('Successfully registered')
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=regForm)
