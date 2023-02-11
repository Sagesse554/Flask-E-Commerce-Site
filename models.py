from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

def ModelCreation(app):

    app = Flask(__name__)
    db = SQLAlchemy(app)
    
    class Users(UserMixin, db.Model):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(120), nullable=False)
        
        def __repr__(self):
            return f"<Users {self.id} {self.username} {self.email} {self.password}>"
        
        def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password = password

    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    return app