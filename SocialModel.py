from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Social(db.Model):
    __tablename__ = 'social'
    id = db.Column(db.Integer, primary_key=True)
    twitter = db.Column(db.String(300))
    instagram = db.Column(db.String(300))
    github = db.Column(db.String(300))
    googleplus = db.Column(db.String(300))

