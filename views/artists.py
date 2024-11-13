from flask import Blueprint, render_template, request, jsonify, redirect
from models import db, Artist
import sys

artists_bp = Blueprint('artists', __name__)

@artists_bp.route('/artists')
def get_artists():
    artists = Artist.query.all()
    return render_template('artists.html', artists=artists)

@artists_bp.route('/artists', methods=['POST'])
def create_artist():
    try:
        name=request.form.get('name')
        address=request.form.get('address')
        phone=request.form.get('phone')
        new_artist = Artist(name=name, address=address, phone=phone)
        db.session.add(new_artist)
        db.session.commit()
    except:
        db.session.rollback()
        print(sys.exc_info())
        # return jsonify({'error':'create artist failed'})
    finally:
        db.session.close()
    return redirect('/artists')

@artists_bp.route('/artists/<artist_id>')
def show_artist(artist_id):
    artist = Artist.query.filter_by(id=artist_id).first()
    return render_template('artist.html', artist=artist)

@artists_bp.route('/artists/<artist_id>', methods=['POST'])
def update_artist(artist_id):
    try:
        artist = Artist.query.filter_by(id=artist_id).first()
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        if artist:
            db.session.query(Artist).filter_by(id=artist_id).update({'name':name, 'address':address, 'phone':phone})
            db.session.commit()
            return redirect(f'/artists/{artist_id}')        
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'updating artist failed'})
    finally:
        db.session.close()

@artists_bp.route('/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    try:
        artist = Artist.query.filter_by(id=artist_id).first()
        if artist:
            db.session.delete(artist)
            db.session.commit()
            return jsonify({'message':'artist deleted'})
        else:
            return jsonify({'error':'artist not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'failed to delete artist'})
    finally:
        db.session.close()