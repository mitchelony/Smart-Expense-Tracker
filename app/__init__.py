from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Make sure to import SQLAlchemy
from config import Config

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load the configuration for the app, including the database URI
    app.config.from_object(Config)  # Loads configuration settings from config.py
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)  # Bind the db object to the app

    # Register your blueprint
    from .routes import main
    app.register_blueprint(main)

    return app