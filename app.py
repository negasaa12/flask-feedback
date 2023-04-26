from datetime import datetime
from flask import Flask, request, redirect, render_template, flash
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

    form = RegisterForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        username = form.username.data

        new_user = User.register(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        db.session.commit()

        return redirect('/secrets')
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=["POST", "GET"])
def login_user():

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            return redirect('/secrets')
        else:
            return render_template('login.html', form=form)

    # if form not submitted or is invalid, render login template with form
    return render_template('login.html', form=form)


@app.route('/secrets')
def secret():

    return "YOU MADE IT"
