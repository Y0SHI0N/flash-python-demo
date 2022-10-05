from flask import Blueprint, render_template
from .models import Destination, Comment


bp = Blueprint('destination', __name__, url_prefix='/destinations')


@bp.route('/<destNr>')
def show(destNr):
    destination = get_destination()[int(destNr)]
    return render_template('destinations/show.html', dest=destination)


def get_destination():
    cmt1 = Comment()
    cmt1.user = "Scott"
    cmt1.text = "10/10"

    cmt2 = Comment()
    cmt2.user = "Jay"
    cmt2.text = "9/10"

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
