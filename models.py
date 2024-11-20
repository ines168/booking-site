from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venues'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    city=db.Column(db.String, nullable=False)
    state=db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    image_link = db.Column(db.String, nullable=False)
    website_link = db.Column(db.String)
    facebook_link = db.Column(db.String)
    shows = db.relationship('Show', backref='venue', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f'<Venue: {self.name}>'


class Artist(db.Model):
    __tablename__ = 'artists'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    city=db.Column(db.String, nullable=False)
    state=db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    image_link = db.Column(db.String, nullable=False)
    website_link = db.Column(db.String)
    facebook_link = db.Column(db.String)
    shows=db.relationship('Show', backref='artist', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f'<Artist: {self.name}>'

class Show(db.Model):
    __tablename__ = 'shows'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=True)
    start_time=db.Column(db.DateTime)
    venue_id=db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    artist_id=db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)