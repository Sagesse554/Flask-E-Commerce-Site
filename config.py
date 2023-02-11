from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config:
    app = Flask(__name__)
    
    db = SQLAlchemy()
    SECRET_KEY = "SagcretKey"
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///EComSite.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}