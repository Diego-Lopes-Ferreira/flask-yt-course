from app import theApp
from flask import render_template

from app.models.forms import TouliterLogin

@theApp.route('/user/<user>')
@theApp.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html', user=user)

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
