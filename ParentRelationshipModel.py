from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class Parentrelationship(db.Model):
    __tablename__ = 'parent_relationship'
    id = db.Column(db.Integer, primary_key=True)
    parent_relationship = db.Column(db.String(300))