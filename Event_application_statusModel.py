from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class ApplicationStat(db.Model):
    __tablename__ = 'application_status'
    status_id = db.Column(db.Integer, primary_key=True)
    application_status = db.Column(db.String(300))
    # Accepted| rejected | RSVP:waiting | RSVP:CONFIRMED | RSVP:rejected

