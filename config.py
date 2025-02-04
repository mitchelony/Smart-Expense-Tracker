import os

class Config:
    SECRET_KEY = os.urandom(24)  # Optional, but good for security
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Path to your SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables overhead