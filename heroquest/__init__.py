import os

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv(find_dotenv())

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    init_config(app)
    init_extensions(app)
    init_views(app)

    return app


def init_config(app):
    app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]


def init_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)

    from .models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


def init_views(app):
    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .views.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
