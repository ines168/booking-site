from collections import defaultdict
from flask import Blueprint, flash, request, jsonify, redirect, url_for, render_template
from sqlalchemy import func
from models import db, Venue
from forms import VenueForm
import sys

venues_bp = Blueprint('venues', __name__)

@venues_bp.route('/venues')
def get_venues():
    venues = Venue.query.all()
    venues_by_city = defaultdict(list)
    form = VenueForm()
    for venue in venues:
        city = venue.city.strip().title()
        venues_by_city[city].append({'id':venue.id, 'name':venue.name})
    return render_template('venues.html', venues_by_city=venues_by_city, form=form)

@venues_bp.route('/venues', methods=['POST'])
@venues_bp.route('/venues/create', methods=['GET', 'POST'])
def create_venue():
    form = VenueForm()
    if request.method == 'GET':
        return render_template('venue_new.html', form=form)
    else:
        if form.validate_on_submit():
            new_venue = Venue(
                name=form.name.data,
                city=form.city.data,
                state=form.state.data,
                address = form.address.data,
                phone = form.phone.data,
                image_link = form.image_link.data,
                website_link = form.website_link.data,
                facebook_link = form.facebook_link.data
            )
            data = new_venue
            try:
                db.session.add(new_venue)
                db.session.commit()
                flash('Venue successfully created!', category='success')
                return redirect(f'/venues/{data.id}')
            except:
                db.session.rollback()
                print(sys.exc_info())
                flash('Couldnt create venue!', category='danger')
            finally:
                db.session.close()
        else:
            print(form.errors)
            flash('Form not validated. Try again!', category='danger')
        return redirect('/venues/create')

@venues_bp.route('/venues/<venue_id>')
def show_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    if venue is None:
        flash('Couldnt find that venue.', category='danger')
        return redirect('/venues')
    form = VenueForm(obj=venue)
    return render_template('venue.html', venue=venue, form=form)

@venues_bp.route('/venues/<venue_id>/edit')
def update_venue_get(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    form = VenueForm(obj=venue)
    return render_template('venue_edit.html', form=form)

@venues_bp.route('/venues/<venue_id>', methods=['POST'])
def update_venue(venue_id):
    venue = Venue.query.filter_by(id=venue_id).first()
    if venue is None:
        flash('Couldnt find that venue.', category='danger')
        return redirect('/venues')
    form = VenueForm()
    if form.validate_on_submit():
        venue.name=form.name.data,
        venue.city=form.city.data,
        venue.state=form.state.data,
        venue.address = form.address.data,
        venue.phone = form.phone.data,
        venue.image_link = form.image_link.data,
        venue.website_link = form.website_link.data,
        venue.facebook_link = form.facebook_link.data
        try:
            db.session.commit()
            flash('Successfully updated the venue!', category='success')
            return redirect(f'/venues/{venue_id}')
        except:
            db.session.rollback()
            print(sys.exc_info())
            flash('Couldnt update the venue.', category='danger')
        finally:
            db.session.close()
    else:
        print(form.errors)
        flash('Form not validated. Try again!', category='danger')
    return redirect(f'/venues/{venue_id}/edit')

@venues_bp.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    try:
        venue = Venue.query.filter_by(id=venue_id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()
            flash('Succefully deleted', category='success')
            return jsonify({'message':'venue deleted'})
        else:
            return jsonify({'error':'venue not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'deleting venue failed'})
    finally:
        db.session.close()