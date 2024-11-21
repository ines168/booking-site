from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, URL
from models import Artist

class ArtistForm(FlaskForm):
    name = StringField(label='Artist Name:', validators=[Length(min=2, max=30), DataRequired()])
    city = StringField(label='City:', validators=[Length(min=2, max=30), DataRequired()])
    state = StringField(label='State:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=4, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=6, max=16), DataRequired()])
    image_link = StringField(label='Image URL:', validators=[DataRequired(), URL()])
    website_link = StringField(label='Website URL:', validators=[DataRequired(), URL()])
    facebook_link = StringField(label='Facebook URL:', validators=[DataRequired(), URL()])

class VenueForm(FlaskForm):
    name = StringField(label='Venue Name:', validators=[Length(min=2, max=30), DataRequired()])
    city = StringField(label='City:', validators=[Length(min=2, max=30), DataRequired()])
    state = StringField(label='State:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=4, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=6, max=16), DataRequired()])
    image_link = StringField(label='Image URL:', validators=[DataRequired(), URL()])
    website_link = StringField(label='Website URL:', validators=[DataRequired(), URL()])
    facebook_link = StringField(label='Facebook URL:', validators=[DataRequired(), URL()])

class ShowForm(FlaskForm):
    name = StringField(label='Event Name:', validators=[Length(min=2, max=30)])
    venue_id = StringField(label='Venue ID:', validators=[DataRequired()])
    artist_id = StringField(label='Artist ID:', validators=[DataRequired()])
    start_time = DateTimeField(label='Start time:', validators=[DataRequired()])

class CreateArtist(FlaskForm):
    def validate_name(self, name_to_check):
        artist = Artist.query.filter_by(name=name_to_check.data).first()
        if artist:
            raise ValidationError('Artist with this name already exists.')
    name = StringField(label='Artist Name:', validators=[Length(min=2, max=30), DataRequired()])
    city = StringField(label='City:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=4, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=6, max=16), DataRequired()])
    submit = SubmitField(label='Create Artist')

class UpdateArtist(FlaskForm):
    def __init__(self, artist_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.artist_id = artist_id

    def validate_name(self, name_to_check):
        print(name_to_check)
        artist = Artist.query.filter_by(name=name_to_check.data).first()
        if artist and artist.id!=self.artist_id:
            raise ValidationError('Artist with this name already exists.')
    name = StringField(label='Artist Name:', validators=[Length(min=2, max=30), DataRequired()])
    address = StringField(label='Address:', validators=[Length(min=4, max=30), DataRequired()])
    phone = StringField(label='Phone:', validators=[Length(min=6, max=16), DataRequired()])
    submit = SubmitField(label='Update Artist')