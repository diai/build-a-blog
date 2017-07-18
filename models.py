#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# July 2017
# Flask Blog App Continued re: LaunchCode
# Rubric: _Project rubric_: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from datetime import datetime
from app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(10000))
    date = db.Column(db.DateTime)

    def __init__(self, title, body, date=None):
        self.title = title
        self.body = body
        if date is None:
            date = datetime.utcnow()
        self.date = date
