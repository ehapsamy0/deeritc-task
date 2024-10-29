import os
from flask import Flask
from dotenv import load_dotenv
from flask_restx import Api
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .extensions import db, jwt, migrate
from .controllers.auth_controller import auth_ns
from app.controllers.book_controller import book_ns


load_dotenv()


def create_app(config_name="development"):
    app = Flask(__name__)

    if config_name == "production":
        app.config.from_object(ProductionConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    api = Api(
        app,
        doc="/api/docs",
        title="BookNest API",
        version="1.0",
        description="API Documentation for BookNest",
        authorizations={
            "Bearer Auth": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                "description": "Add 'Bearer <JWT token>' to authenticate",
            }
        },
    )

    api.add_namespace(auth_ns, path="/api/auth")
    api.add_namespace(book_ns, path="/api/books")

    with app.app_context():
        db.create_all()

    return app
