from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from typing import Any

db = SQLAlchemy(app)


class ApiUsers(db.Model):
    __tablename__ = 'api_users'
    #role_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(300), unique=True, nullable=False)
    email = db.Column(db.String(300))
    job_tittle = db.Column(db.String(300))
    #role = db.Column(db.String(300))
    password = db.Column(db.String(300), nullable=False)

    def _repr_(self):
        return str({
            'username': self.username,
            'password': self.password
        })

    def username_password_match(_username, _password):
        user = User.query.filter_by (username=_username).filter_byy (password=_password).first()
        if user is None:
            return False
        else:
            return True

    def getAllUsers(self):
        return User.query.all()

    def createUser(self, _username, _password, _email):
        new_user = User(self, username=_username, password=_password, email=_email)
        db.session.add(new_user)
        db.session.commit()
