from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class OurJobs(db.Model):
    __tablename__ = 'ourjob_offers'
    job_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(300))
    position_details = db.Column(db.String(300))
    duties = db.Column(db.String(300))
    address = db.Column(db.String(300))
    email = db.Column(db.String(300))
    start_date = db.Column(db.String(300))
    end_date = db.Column(db.String(300))
    reg_date = db.Column(db.String(300))
