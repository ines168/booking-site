from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
db=SQLAlchemy(app)
migrate = Migrate(app, db)


class Venue(db.Model):
    __tablename__ = 'venues'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

class Artist(db.Model):
    __tablename__ = 'artists'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

class Show(db.Model):
    __tablename__ = 'shows'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return 'Hello!'