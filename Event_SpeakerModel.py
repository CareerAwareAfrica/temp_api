from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Speakers(db.Model):
    __tablename__ = 'event_speakers'
    # from event table
    event_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(300))
    email = db.Column(db.String(300))
    topic_tittle = db.Column(db.String(300))
    topic_desc = db.Column(db.String(300))
    meta_data = db.Column(db.String(300))
