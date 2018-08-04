from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class DonateType(db.Model):
    __tablename__ = 'donate_type'
    # from event table
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(300))
