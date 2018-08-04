from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\cleopatra.douglas\\Desktop\\plural\\career.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False