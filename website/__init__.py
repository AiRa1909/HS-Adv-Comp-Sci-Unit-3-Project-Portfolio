from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aisyah'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # tell Flask where to save the database file
    db.init_app(app)
    # connect database!

    from .views import views
    from website.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # import and register all the routes

    create_database(app)
    # run the function to create the database file if it doesn't exist

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        # I must import models here so the database knows what tables to create
        from .models import Sesh
        with app.app_context():
            db.create_all()
        print("Created database!")