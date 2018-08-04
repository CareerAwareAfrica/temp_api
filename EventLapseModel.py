from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventLapse(db.Model):
    __tablename__ = 'eventlapse'
    lapse_id = db.Column(db.Integer, primary_key=True)
    event_lapse = db.Column(db.Integer)
    # 1=upcoming 2=past 3=ongoingrg 4=onginevnt
