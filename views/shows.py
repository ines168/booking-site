from flask import Blueprint, render_template, redirect, request, jsonify
from models import Show, db
import sys

shows_bp = Blueprint('shows', __name__)

@shows_bp.route('/shows')
def get_shows():
    shows = Show.query.all()
    return render_template('shows.html', shows=shows)

@shows_bp.route('/shows', methods=['POST'])
def create_show():
    try:
        name = request.form.get('name')
        artistId = request.form.get('artistId')
        venueId = request.form.get('venueId')
        show = Show(name=name, artist_id=artistId, venue_id=venueId)
        db.session.add(show)
        db.session.commit()
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'create show failed'})
    finally:
        db.session.close()
    return redirect('/shows')

@shows_bp.route('/shows/<show_id>')
def show_show(show_id):
    show = Show.query.filter_by(id=show_id).first()
    return render_template('show.html', show=show)

@shows_bp.route('/shows/<show_id>', methods=['POST'])
def update_show(show_id):
    try:
        name = request.form.get('name')
        artistId = request.form.get('artistId')
        venueId = request.form.get('venueId')
        show = Show.query.filter_by(id=show_id).first()
        if show:
            db.session.query(Show).filter_by(id=show_id).update({'name':name, 'artist_id':artistId, 'venue_id':venueId})
            db.session.commit()
            return redirect(f'/shows/{show_id}')
        else:
            return jsonify({'error':'show not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'show update failed'})
    finally:
        db.session.close()

@shows_bp.route('/shows/<show_id>', methods=['DELETE'])
def delete_show(show_id):
    try:
        show = Show.query.filter_by(id=show_id).first()
        if show:
            db.session.delete(show)
            db.session.commit()
            return jsonify({'message':'deleted show successfully'})
        else:
            return jsonify({'error':'couldnt find show'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'delete show failed'})
    finally:
        db.session.close()
