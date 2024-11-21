from flask import Blueprint, flash, render_template, redirect, request, jsonify
from models import Show, db
from forms import ShowForm
import sys

shows_bp = Blueprint('shows', __name__)

@shows_bp.route('/shows')
def get_shows():
    shows = Show.query.all()
    form = ShowForm()
    return render_template('shows.html', shows=shows, form=form)

@shows_bp.route('/shows', methods=['POST'])
def create_show():
    form = ShowForm()
    if form.validate_on_submit():
        show = Show(
            name=form.name.data,
            artist_id=form.artist_id.data,
            venue_id=form.venue_id.data,
            start_time=form.start_time.data
        )
        try:
            db.session.add(show)
            db.session.commit()
            flash('Succesffully created a show!', category='success')
            return redirect(f'/shows/{show.id}')
        except:
            db.session.rollback()
            print(sys.exc_info())
            flash('Error creating a show.', category='danger')
        finally:
            db.session.close()
    else:
        flash('Error validating the form.', category='danger')
    return redirect('/shows')

@shows_bp.route('/shows/<show_id>')
def show_show(show_id):
    show = Show.query.filter_by(id=show_id).first()
    if show is None:
        flash('Couldnt find that show.', category='danger')
        return redirect('/shows')
    form = ShowForm(obj=show)
    return render_template('show.html', show=show, form=form)

@shows_bp.route('/shows/<show_id>', methods=['POST'])
def update_show(show_id):
    show = Show.query.filter_by(id=show_id).first()
    if show is None:
        flash('No such show.', category='danger')
        return redirect('/shows')
    form = ShowForm(obj=show)
    if form.validate_on_submit():
        show.name = form.name.data
        show.artist_id = form.artist_id.data
        show.venue_id = form.venue_id.data
        show.start_time = form.start_time.data
        try:
            # db.session.query(Show).filter_by(id=show_id).update({'name':name, 'artist_id':artistId, 'venue_id':venueId})
            db.session.commit()
            flash('Successfully updated the show!', category='success')
            return redirect(f'/shows/{show_id}')
        except:
            db.session.rollback()
            print(sys.exc_info())
            flash('Error updating the show.', category='danger')
            return redirect('/shows')
        finally:
            db.session.close()
    else:
        print(form.errors)
        flash('Error validating form.', category='danger')
        return redirect('/shows')

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
