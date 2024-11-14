from collections import defaultdict
from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from sqlalchemy import func
from models import db, Venue
import sys

venues_bp = Blueprint('venues', __name__)

@venues_bp.route('/venues')
def get_venues():
    venues = Venue.query.all()
    venues_by_city = defaultdict(list)
    for venue in venues:
        city = venue.city.strip().title()
        venues_by_city[city].append({'id':venue.id, 'name':venue.name})
    return render_template('venues.html', venues_by_city=venues_by_city)

@venues_bp.route('/venues', methods=['POST'])
def create_venue():
    try:
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        phone = request.form.get('phone')
        new_venue = Venue(name=name, address=address, phone=phone, city=city)
        db.session.add(new_venue)
        db.session.commit()
    except:
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    return redirect('/venues')

@venues_bp.route('/venues/<venue_id>')
def show_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    return render_template('venue.html', venue=venue)

@venues_bp.route('/venues/<venue_id>', methods=['POST'])
def update_venue(venue_id):
    try:
        venue = Venue.query.filter_by(id=venue_id).first()
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
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
            "phone": phone, "city":city
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

@venues_bp.route('/venues/<venue_id>', methods=['DELETE'])
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