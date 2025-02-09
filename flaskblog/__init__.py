from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '900508fd00cb981a1f2587ded1f215ef'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(BASE_DIR, 'site.db')}"
db = SQLAlchemy(app)

from flaskblog import routes