from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventSite(db.Model):
    __tablename__ = 'event_site'
    event_id = db.Column(db.Integer, primary_key=True)
    # from event table
    event_name = db.Column(db.String(300))
    event_main_picture = db.Column(db.String(300))
    event_photo_credit = db.Column(db.String(300))
    event_photo_url = db.Column(db.String(300))
    event_tittle = db.Column(db.String(300))
    event_description = db.Column(db.String(300))
    event_site_color = db.Column(db.String(300))
    custom_css_rules = db.Column(db.String(300))
    event_site_published = db.Column(db.Integer)
