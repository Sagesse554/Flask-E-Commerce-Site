from flask import Flask
from app.routes.authentication import *
from app.routes.main import *
from flask_login import LoginManager, login_required
from app.models import ModelCreation

def AppCreation():

    app = Flask(__name__)

    app = ModelCreation(app)

    app.route('/login', methods=['GET', 'POST'])(login)
    app.route('/signup', methods=['GET', 'POST'])(signup)
    app.route('/logout')(logout)
    app.route('/', methods=['GET', 'POST'])(index)
    app.route('/profile', methods=['GET', 'POST'])(login_required(profile))
    
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app