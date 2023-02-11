from flask import render_template
from flask_login import current_user

def index():
    return render_template('main/index.html')

def profile():
    return render_template('main/profile.html', name = current_user.username)