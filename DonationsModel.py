from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Donations(db.Model):
    __tablename__ = 'donations'
    # from event table
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer)
    donor = db.Column(db.String(300))
    tittle = db.Column(db.String(300))
    mobile_number = db.Column(db.String(300))
    care_package = db.Column(db.Integer)
    # 1= yes 2= no
    address = db.Column(db.String(300))
    email = db.Column(db.String(300))
    amount = db.Column(db.String(300))
    recurring = db.Column(db.Integer)
    last_donate_date = db.Column(db.String(300))
    next_donate_date = db.Column(db.String(300))
