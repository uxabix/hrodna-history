import os

from flask import Flask
from flask_bootstrap import Bootstrap5

from .database import db
import config

bootstrap = Bootstrap5()


def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.jinja_options["comment_start_string"] = "{="
    app.jinja_options["comment_end_string"] = "=}"

    bootstrap.init_app(app)
    db.init_app(app)

    if not os.path.exists("logs"):
        os.mkdir("logs")

    from app.main import bp as main_bp
    from app.article import bp as article_bp

    app.register_blueprint(article_bp, url_prefix="/article")
    app.register_blueprint(main_bp)

    return app
