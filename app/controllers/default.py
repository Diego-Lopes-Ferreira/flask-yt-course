from app import theApp
from flask import render_template

from app.models.forms import TouliterLogin

@theApp.route('/index')
@theApp.route('/')
def index():
    return render_template('index.html')

@theApp.route('/home')
def home():
    return render_template('index.html')

@theApp.route('/test/')
@theApp.route('/test/<name>/')
def anotherOne(name=None):
    if name:
        return 'Hello, %s :)' % name
    else:
        return 'Oh, hi, please identify'


@theApp.route('/login', methods=['GET', 'POST'])
def Login():
    form = TouliterLogin()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        print(form.rememberMe.data)
    else:
        print(form.errors)

    return render_template('login.html', form=form)
