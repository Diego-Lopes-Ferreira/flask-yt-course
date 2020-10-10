from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class TouliterLogin(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    rememberMe = BooleanField('rememberMe', validators=[])