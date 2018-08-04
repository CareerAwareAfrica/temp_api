from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EnterprisePartner(db.Model):
    __tablename__ = 'enterprise_partners'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(300))
    email = db.Column(db.String(300))
    job_tittle = db.Column(db.String(300))
    enterprise_name = db.Column(db.String(300))
    pwd = db.Column(db.String(300))
    verified = db.Column(db.Integer)
