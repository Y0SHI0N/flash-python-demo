from flask import Blueprint, render_template, request, url_for, redirect, flash
from .form import DestinationForm
from . import db
from .models import Destination, User


mainbp = Blueprint('main', __name__, url_prefix='/')


@mainbp.route('/')
def index():
    tag_line = 'You need a vacation'
    destinations = Destination.query.all()  # get the hotels
    return render_template('index.html', tag_line=tag_line, destinations=destinations)


@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        destinations = Destination.query.filter(
            Destination.description.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
