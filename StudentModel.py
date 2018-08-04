from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Donations(db.Model):
    __tablename__ = 'donations'
    # from event table
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(300))
    last_name = db.Column(db.String(300))
    username = db.Column(db.String(300))
    mobile_number = db.Column(db.String(300))
    address = db.Column(db.String(300))
    email = db.Column(db.String(300))
    date_of_birth = db.Column(db.String(300))
    reg_date = db.Column(db.String(300))
