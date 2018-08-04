from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventStat(db.Model):
    __tablename__ = 'event_statistics'
    # from event table
    event_id = db.Column(db.Integer, primary_key=True)
    number_of_applicants = db.Column(db.Integer)
    number_of_attendees = db.Column(db.Integer)
