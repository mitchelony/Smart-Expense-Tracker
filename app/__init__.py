from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Load the configuration for the app, including the database URI
    app.config.from_object(Config)  # Loads configuration settings from config.py
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)  # Bind the db object to the app

    # Keep your original blueprint registration logic intact
    from .routes import main
    app.register_blueprint(main)

    return app