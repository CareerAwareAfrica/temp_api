from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Coach(db.Model):
    __tablename__ = 'event_coach'
    # from event table
    event_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(300))
    email = db.Column(db.String(300))
    twitter_handle = db.Column(db.String(300))
    photo = db.Column(db.String(300))
    url = db.Column(db.String(300))
