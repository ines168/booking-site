from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
import sys

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
db=SQLAlchemy(app)
migrate = Migrate(app, db)


class Venue(db.Model):
    __tablename__ = 'venues'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    # city, state, link

    def __repr__(self):
        return f'<Venue: {self.name}>'


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

@app.route('/venues')
def get_venues():
    venues = Venue.query.all()
    return render_template('venues.html', venues=venues)

@app.route('/venues', methods=['POST'])
def create_venue():
    try:
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        new_venue = Venue(name=name, address=address, phone=phone)
        db.session.add(new_venue)
        db.session.commit()
    except:
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    return redirect('/venues')

@app.route('/venues/<venue_id>')
def show_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    return render_template('venue.html', venue=venue)

@app.route('/venues/<venue_id>', methods=['POST'])
def update_venue(venue_id):
    try:
        venue = Venue.query.filter_by(id=venue_id).first()
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        # data = request.get_json()
        # name = data.get('name')
        # address = data.get('address')
        # phone = data.get('phone')
        if venue:
            # venue.name=name
            # venue.address = address
            # venue.phone = phone
            db.session.query(Venue).filter_by(id=venue_id).update({
            "name": name,
            "address": address,
            "phone": phone
        })
            db.session.commit()
            return redirect(f'/venues/{venue_id}')
        else:
            return jsonify({'error':'venue not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'updating venue failed'})
    finally:
        db.session.close()

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    try:
        venue = Venue.query.filter_by(id=venue_id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()
            return jsonify({'message':'venue deleted'})
        else:
            return jsonify({'error':'venue not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'deleting venue failed'})
    finally:
        db.session.close()
    # return redirect('/venues')

@app.route('/')
def index():
    return render_template('layout.html')