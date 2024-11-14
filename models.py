from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venues'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    shows = db.relationship('Show', backref='venues', lazy=True, cascade='all, delete-orphan')
    # state, link

    def __repr__(self):
        return f'<Venue: {self.name}>'


class Artist(db.Model):
    __tablename__ = 'artists'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    phone=db.Column(db.String, nullable=False)
    shows=db.relationship('Show', backref='artists', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Artist: {self.name}>'

class Show(db.Model):
    __tablename__ = 'shows'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=True)
    date=db.Column(db.String, nullable=True)
    venue_id=db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    artist_id=db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)