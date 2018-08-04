from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_tittle = db.Column(db.String(300))
    event_description = db.Column(db.String(300))
    event_type = db.Column(db.Integer)
    event_venue = db.Column(db.String(300))
    event_regdate = db.Column(db.String(300))
    event_startdate = db.Column(db.String(300))
    event_enddate = db.Column(db.String(300))
    event_duration = db.Column(db.String(300))
    event_email = db.Column(db.String(300))
    audience_size = db.Column(db.Integer)
    event_stats = db.Column(db.Integer)
    event_starttime = db.Column(db.String(300))
    event_url = db.Column(db.String(300))
    event_endtime = db.Column(db.String(300))
    event_city = db.Column(db.String(300))
    event_country = db.Column(db.String(300))
    event_lapse = db.Column(db.Integer)
    # event_lapse integer should corresponde with integers in event_lapse table.
    invite_status = db.Column(db.Integer)
    # invite_status integer should corresponde with integers in invite status table.
    verified = db.Column(db.Integer)
