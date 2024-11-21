from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from models import db, Artist
import sys
from forms import ArtistForm

artists_bp = Blueprint('artists', __name__)

@artists_bp.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    form = ArtistForm() 
    return render_template('artists.html', artists=artists, form=form) 

@artists_bp.route('/artists', methods=['POST'])
@artists_bp.route('/artists/create', methods=['GET', 'POST'])
def create_artist():
    form = ArtistForm()
    if request.method == 'GET':
        return render_template('artist_new.html', form=form)
    if form.validate_on_submit():
        artist = Artist(
            name=form.name.data,
            address=form.address.data,
            phone=form.phone.data,
            city=form.city.data,
            state=form.state.data,
            image_link = form.image_link.data,
            website_link = form.website_link.data,
            facebook_link = form.facebook_link.data
        )
        try:
            db.session.add(artist)
            db.session.commit()
            flash('Artist successfully created!', category='success')
            return redirect(f'/artists/{artist.id}')
        except:
            db.session.rollback()
            print(sys.exc_info())
            flash('Error creating artist', category='danger')
        finally:
            db.session.close()
            return redirect('/artists')
    else:
    # if form.errors != {}:
    #     for err_msg in form.errors.values():
    #         flash(f'there was an error: {err_msg}', category='danger')
        for field, errors in form.errors.items():
            for err_msg in errors:
                flash(f'There was an error validating {field}: {err_msg}', category='danger')
        return redirect('/artists/create')

@artists_bp.route('/artists/<artist_id>')
def show_artist(artist_id):
    artist = Artist.query.filter_by(id=artist_id).first()
    if artist is None:
        flash('That artist doesnt exist. Try again!', category='danger')
        return redirect('/artists')
    form = ArtistForm(artist_id=artist.id, obj=artist)
    return render_template('artist.html', artist=artist, form=form)

@artists_bp.route('/artists/<artist_id>', methods=['POST'])
def update_artist(artist_id):
    artist = Artist.query.filter_by(id=artist_id).first()
    if artist is None:
        flash('That artist doesnt exist. Try again!', category='danger')
        return redirect('/artists')
    form = ArtistForm(artist_id=artist.id, obj=artist)
    if form.validate_on_submit():
        try:
            db.session.query(Artist).filter_by(id=artist_id).update({'name':form.name.data, 'address':form.address.data, 'phone':form.phone.data})
            db.session.commit()
            flash('Successfully updated artist!', category='success')
        except:
            db.session.rollback()
            print(sys.exc_info())
            flash('Error updating artist', category='danger')
        finally:
            db.session.close()
        return redirect(f'/artists/{artist_id}') 
    else:
        for field, errors in form.errors.items():
            for err_msg in errors:
                flash(f'There was an error: {err_msg}', category='danger')
        return redirect('/artists')


@artists_bp.route('/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    try:
        artist = Artist.query.filter_by(id=artist_id).first()
        if artist:
            db.session.delete(artist)
            db.session.commit()            
            flash('Succefully deleted', category='success')
            return jsonify({'message':'artist deleted'})
        else:
            return jsonify({'error':'artist not found'})
    except:
        db.session.rollback()
        print(sys.exc_info())
        return jsonify({'error':'failed to delete artist'})
    finally:
        db.session.close()