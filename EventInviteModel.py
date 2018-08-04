from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class EventInvite(db.Model):
    __tablename__ = 'event_invite'
    invite_id = db.Column(db.Integer, primary_key=True)
    invite_status = db.Column(db.String(300))
# invite_status is on or off
