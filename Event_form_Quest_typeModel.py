from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class FormQuestion(db.Model):
    __tablename__ = 'form_questions'
    question_type_id = db.Column(db.Integer)
    question_type = db.Column(db.String(300))
