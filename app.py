from flask import Flask, jsonify, redirect, render_template, request
from models import db, Venue, Artist
from views import venues_bp, artists_bp
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
import sys

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(venues_bp)
app.register_blueprint(artists_bp)

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return render_template('layout.html')