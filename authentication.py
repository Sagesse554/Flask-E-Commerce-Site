from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from app.models import Users

db = SQLAlchemy()

def login():
    if request.method == 'GET':
        return render_template('authentication/login.html')
    else:
        usname = request.form.get('username')
        psword = request.form.get('password')

        user = Users.query.filter_by(username = usname).first()

        if (user is None) or (not check_password_hash(user.password, psword)):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('profile'))

def signup():
    if request.method == 'GET':
        return render_template('authentication/register.html')
    else:
        eml = request.form.get('email')
        usname = request.form.get('username')
        psword = request.form.get('password')
        psword2 = request.form.get('password2')

        user = Users.query.filter_by(email = eml).first()

        if len(eml) < 10:
            flash("Email length must not be less than 4 characters", category="error")
            return redirect(url_for('signup'))
        elif len(usname) < 4:
            flash("Username length must not be less than 2 characters", category="error")
            return redirect(url_for('signup'))
        elif len(psword) < 8:
            flash("Password length must be at least 8 characters", category="error")
            return redirect(url_for('signup'))
        elif psword != psword2:
            flash("Password and confirmation don't match")
            return redirect(url_for('signup'))
        elif user != None:
            flash('Email address already exists')
            return redirect(url_for('signup'))
        else:
            flash("Account created successfully", category="success")
            new_user = Users(username = usname, email=eml, password=generate_password_hash(psword, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            user = Users.query.filter_by(email = eml).first()
            return redirect(url_for('profile'))

def logout():
    logout_user()
    return redirect(url_for('index'))