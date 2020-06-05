from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
from enums import Genres, States
from validators import multiple_field_validation


class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )


class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[
            DataRequired(),
            AnyOf([choice.value for choice in States])
        ],
        choices=States.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    genres = SelectMultipleField(
        'genres', validators=[
            DataRequired(),
            multiple_field_validation([choice.value for choice in Genres])
        ],
        choices=Genres.choices()
    )
    website = StringField(
        'website', validators=[DataRequired(), URL()]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[DataRequired(), URL()]
    )
    seeking_talent = BooleanField(
        'seeking_talent'
    )
    seeking_description = StringField(
        'seeking_description'
    )


class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[
            DataRequired(),
            AnyOf([choice.value for choice in States])
        ],
        choices=States.choices()
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    genres = SelectMultipleField(
        'genres', validators=[
            DataRequired(),
            multiple_field_validation([choice.value for choice in Genres])
        ],
        choices=Genres.choices()
    )
    website = StringField(
        'website', validators=[URL()]
    )
    image_link = StringField(
        'image_link', validators=[URL()]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    seeking_venue = BooleanField(
        'seeking_venue'
    )
    seeking_description = StringField(
        'seeking_description'
    )