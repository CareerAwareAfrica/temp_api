from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventSections(db.Model):
    __tablename__ = 'event_site_sections'
    section_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    # from event table
    section_name = db.Column(db.String(300))
    content = db.Column(db.String(300))
    background = db.Column(db.String(300))
    is_public = db.Column(db.String(300))

