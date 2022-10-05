from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Destination, Comment, UserMixin, User
from .form import DestinationForm, commentForm
from . import db
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os


bp = Blueprint('destination', __name__, url_prefix='/destinations')


@bp.route('/<destNr>')
def show(destNr):
    cform = commentForm()
    dest = Destination.query.filter_by(id=destNr).first()
    return render_template('destinations/show.html', destination=dest, form=cform)


@bp.route('/<destNr>/comment', methods=['GET', 'POST'])
def comment(destNr):
    # here the form is created  form = CommentForm()
    form = commentForm()
    # get the destination object associated to the page and the comment
    destination_obj = Destination.query.filter_by(id=destNr).first()
    if form.validate_on_submit():  # this is true only in case of POST method
        # read the comment from the form
        comment = Comment(comment=form.cmt.data,
                          destination=destination_obj)
        # here the back-referencing works - comment.destination is set
        # and the link is created
        db.session.add(comment)
        db.session.commit()
        print("The following comment has been posted:", form.cmt.data)
        print("current id: ", destNr)
    # notice the signature of url_for
    return redirect(url_for('destination.show', destNr=destNr))


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)

    if current_user.usertype != 'admin':
        flash("Need administrator login")
        return redirect(url_for('auth.login'))

    else:
        form = DestinationForm()
        if form.validate_on_submit():
            # call the function that checks and returns image
            db_file_path = check_upload_file(form)
            # create a new hotel with the information passed
            new_destination = Destination(name=form.name.data, description=form.description.data,
                                          image=db_file_path, currency=form.currency.data)
            # when creating a room, pass the hotel and set the attribute
            db.session.add(new_destination)
            db.session.commit()
            print('Successfully created new travel destination', 'success')
            # return redirect(url_for("main.index"))
            return redirect(url_for('destination.create'))
        return render_template('destinations/create.html', form=form)


def check_upload_file(form):
    # get file data from form
    fp = form.image.data
    filename = fp.filename
    # get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path = os.path.join(
        BASE_PATH, 'static/img', secure_filename(filename))
    # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/img/' + secure_filename(filename)
    # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path
