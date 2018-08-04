from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Parents(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(300))
    parent_relationship = db.Column(db.Integer)
    ward_name = db.Column(db.String(300))
    # how do we handle more than one ward?
    address = db.Column(db.String(300))
    city = db.Column(db.String(300))
    country = db.Column(db.String(300))