from flask import Blueprint, render_template, request, url_for, redirect
from .form import DestinationForm

mainbp = Blueprint('main', __name__, url_prefix='/')


@mainbp.route('/')
def index():
    return render_template('index.html')


@mainbp.route('/create', methods=['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    form = DestinationForm()
    if form.validate_on_submit():
        print('Successfully created new travel destination', 'success')
        # return redirect(url_for("main.index"))
        return redirect(url_for('main.create'))
    return render_template('create.html', form=form)
