from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Eventtype(db.Model):
    __tablename__ = 'event_types'
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(300))