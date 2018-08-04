from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class InternshipMessages(db.Model):
    __tablename__ = 'internship_messages'
    id = db.Column(db.Integer, primary_key=True)
    bl_id = db.Column(db.Integer)
    # from business_leader table
    internship_id = db.Column(db.Integer)
    # from internship table
    student_id = db.Column(db.Integer)
    # from student table
    message = db.Column(db.String(300))

