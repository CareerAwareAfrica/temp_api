from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Schools(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(300))
    address = db.Column(db.String(300))
    city = db.Column(db.String(300))
    country = db.Column(db.String(300))
    verified = db.Column(db.Integer)