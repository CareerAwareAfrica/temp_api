from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class FormQuestion(db.Model):
    __tablename__ = 'form_questions'
    form_id = db.Column(db.Integer)
    # from form table
    event_id = db.Column(db.Integer, primary_key=True)
    # from event table
    questions = db.Column(db.String(300))
    help_text = db.Column(db.String(300))
    choices = db.Column(db.String(300))
    multi_choice = db.Column(db.Integer)
    question_type = db.Column(db.Integer)
    is_question_required = db.Column(db.Integer)
    # 1 = yes 2 = no
    order = db.Column(db.Integer)
    # numerically, 0 means top
