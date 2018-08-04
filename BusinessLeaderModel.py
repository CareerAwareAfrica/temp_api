from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class BusinessLeader(db.Model):
    __tablename__ = 'business_Leader'
    bl_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    company_name = db.Column(db.String(300))
    company_type = db.Column(db.String(300))
    about = db.Column(db.String(300))
    address = db.Column(db.String(300))
    city = db.Column(db.String(300))
    country = db.Column(db.String(300))
    verified = db.Column(db.Integer)
