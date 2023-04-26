from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, DataRequired, URL

# Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name.

# Make sure you are using WTForms and that your password input hides the characters that the user is typing!


class RegisterForm(FlaskForm):

    first_name = StringField('First Name', validators=[InputRequired()])

    last_name = StringField('Last Name', validators=[InputRequired()])

    email = StringField('Email', validators=[InputRequired()])

    username = StringField('Username', validators=[InputRequired()])

    password = PasswordField('Password', validators=[InputRequired()])


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired()])

    password = PasswordField('Password', validators=[InputRequired()])
