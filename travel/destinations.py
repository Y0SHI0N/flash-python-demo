from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination, Comment
from .form import commentForm


bp = Blueprint('destination', __name__, url_prefix='/destinations')


@bp.route('/<destNr>')
def show(destNr):
    cform = commentForm()
    destination = get_destination()[int(destNr)]
    return render_template('destinations/show.html', dest=destination, form=cform)


@bp.route('/<destNr>/comment', methods=['GET', 'POST'])
def comment(destNr):
    # here the form is created  form = CommentForm()
    form = commentForm()
    if form.validate_on_submit():  # this is true only in case of POST method
        print("The following comment has been posted:", form.cmt.data)
        print("current id: ", destNr)
    # notice the signature of url_for
    return redirect(url_for('destination.show', destNr=destNr))


def get_destination():
    cmt1 = Comment()
    cmt1.user = "Scott"
    cmt1.text = "definitely coming back next time"

    cmt2 = Comment()
    cmt2.user = "Jay"
    cmt2.text = "definitely coming back next time. also definitely did not copy scott"

    Italy = Destination()
    Italy.name = "Italy"
    Italy.currency = "0.67 EUR"
    Italy.addCommment(cmt1)
    Italy.addCommment(cmt2)

    England = Destination()
    England.name = "England"
    England.currency = "0.67 Pound"
    England.addCommment(cmt1)
    England.addCommment(cmt2)

    France = Destination()
    France.name = "France"
    France.currency = "0.57 EUR"
    France.addCommment(cmt1)
    France.addCommment(cmt2)

    return [Italy, England, France]
