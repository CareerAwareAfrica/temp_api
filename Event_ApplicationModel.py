from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Application(db.Model):
    __tablename__ = 'event_applications'
    event_id = db.Column(db.Integer)
    # from event table
    form_id = db.Column(db.Integer)
    # from form table
    application_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(300))
    application_status = db.Column(db.String(300))
    rsvp = db.Column(db.String(300))
    score = db.Column(db.String(300))
