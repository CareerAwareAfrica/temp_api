from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class AdminUsers(db.Model):
    __tablename__ = 'admin_users'
    role_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(300))
    user_name = db.Column(db.String(300))
    email = db.Column(db.String(300))
    job_tittle = db.Column(db.String(300))
    role = db.Column(db.String(300))
    pwd = db.Column(db.String(300))
