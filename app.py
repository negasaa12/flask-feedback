from datetime import datetime
from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from sqlalchemy import text
from unittest import TestCase
from forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "HELLO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.app_context().push()


connect_db(app)


@app.route('/')
def home():

    return redirect('/register')


@app.route('/register', methods=["POST", "GET"])
def register():
    """Register a New User"""
    form = RegisterForm()

    if request.method == "POST" and form.validate_on_submit():
        # Handle form submission
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        username = form.username.data

        new_user = User.register(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        db.session.commit()

        session['user_id'] = new_user.id

        return redirect('/secrets')
    else:
        # Show the register form
        return render_template('register.html', form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
    """" Log in user"""

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['user_id'] = user.id
            return redirect(f'/users/{user.id}')
    else:
        return render_template('login.html', form=form)


@app.route('/logout')
def logout_user():
    """Log out User"""

    session.pop('user_id')
    return redirect('/')


@app.route('/users/<int:id>')
def user_info(id):
    if "user_id" not in session:
        return redirect('/')

    user = User.query.filter_by(id=id).first_or_404()
    return render_template('users_info.html', user=user)
