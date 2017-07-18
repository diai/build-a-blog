#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# July 2017
# Flask Blog App Continued re: LaunchCode
# Rubric: _Project rubric_: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:123456789@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'super_secret_key'
app.static_folder = 'static'
db = SQLAlchemy(app)
