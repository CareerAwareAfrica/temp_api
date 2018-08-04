from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Testiedu(db.Model):
    __tablename__ = 'testi_edu'
    id = db.Column(db.Integer, primary_key=True)
    featured_image = db.Column(db.String(300))
    edu_name = db.Column(db.String(300))
    edu_tittle = db.Column(db.String(300))
    testimony = db.Column(db.String(300))