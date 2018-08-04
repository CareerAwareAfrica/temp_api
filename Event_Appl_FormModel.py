from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventSite(db.Model):
    __tablename__ = 'event_site'
    event_id = db.Column(db.Integer)
    form_id = db.Column(db.Integer, primary_key=True)
    # from event table
    header = db.Column(db.String(300))
    description = db.Column(db.String(300))
    email_confirm = db.Column(db.String(300))
    form_startdate = db.Column(db.String(300))
    form_enddate = db.Column(db.String(300))
    applicantion_number = db.Column(db.Integer)

