from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Educators(db.Model):
    __tablename__ = 'educators'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(300))
    email = db.Column(db.String(300))
    job_tittle = db.Column(db.String(300))
    school_name = db.Column(db.String(300))
    referer = db.Column(db.String(300))
    pwd = db.Column(db.String(300))
    verified = db.Column(db.Integer)
