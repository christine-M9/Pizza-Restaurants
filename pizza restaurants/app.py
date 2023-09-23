from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initializing  SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
