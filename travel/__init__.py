from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap5


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    app.secret_key = "catchupwithweek8"

    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    return app
