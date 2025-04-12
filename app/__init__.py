from flask import Flask
from Config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from logging.handlers import RotatingFileHandler
import datetime
import logging
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
bootstrap = Bootstrap4(app)
login.login_view = 'login'

if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler(f'logs/myapp_{datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log', maxBytes=10240, backupCount=50)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('MyApp Started')

from app import routes, models, forms, errors
