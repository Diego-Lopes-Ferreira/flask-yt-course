from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

theApp = Flask(__name__)
theApp.config.from_object('config')
db = SQLAlchemy(theApp)
migrate = Migrate(theApp, db)

manager = Manager(theApp)
manager.add_command('db', MigrateCommand)


from app.controllers import default
