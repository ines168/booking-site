from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

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