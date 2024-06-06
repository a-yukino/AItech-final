# forms.py - defines form formats and its restrictions on flaskdb
# Copyright (C) 2024 Yasuhiro Hayashi

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, DateField, DateTimeField, TimeField, FileField, SubmitField, SelectMultipleField

from wtforms.validators import DataRequired, length
from flaskdb.widgets import *

class LoginForm(FlaskForm):
    username = StringField(
        "User Name",
        validators = [
            DataRequired(message="User Name is required."),
            length(max=64, message="User Name should be input within 64 characters."),
        ],
    )
    password = PasswordField(
        "Password",
        validators = [
            DataRequired(message="Password is required."),
        ],
    )
    cancel = ButtonField("Cancel")
    submit = SubmitField("Login")

    def copy_from(self, user):
        self.username.data = user.username
        self.password.data = user.password

    def copy_to(self, user):
        user.username = self.username.data
        user.password = self.password.data

class SpotForm(FlaskForm):
    area = StringField(
        "Area",
        validators = [
        ],
    )
    cityname = StringField(
        "City Name",
        validators = [
        ],
    )
    spotname = StringField(
        "Spot Name",
        validators = [
        ],
    )
    datetime = DateTimeField(
        "Date Time",
        validators = [
        ],
    )
    latitude = FloatField(
        "Latitude",
        validators = [
        ],
    )
    longitude = FloatField(
        "Longitude",
        validators = [
        ],
    )
    url = StringField(
        "URL",
        validators = [
        ],
    )
    picture = FileField(
        "Picture",
        validators = [
        ],
    )
    history_culture = IntegerField(
        "History &amp; Culture",
        validators = [
        ],
    )
    food_product = IntegerField(
        "Food &amp; Product",
        validators = [
        ],
    )
    nature = IntegerField(
        "Nature",
        validators = [
        ],
    )
    views = IntegerField(
        "Views",
        validators = [
        ],
    )
    experience = IntegerField(
        "Experience",
        validators = [
        ],
    )
    opentime = TimeField(
        "Open Time",
        validators = [
        ],
    )
    closetime = TimeField(
        "Close Time",
        validators = [
        ],
    )

    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")

    def copy_from(self, spot):
        self.area.data = spot.area
        self.cityname.data = spot.cityname
        self.spotname.data = spot.spotname
        self.datetime.data = spot.datetime
        self.latitude.data = spot.latitude
        self.longitude.data = spot.longitude
        self.url.data = spot.url
        self.picture.data = spot.picture
        self.history_culture.data = spot.history_culture
        self.food_product.data = spot.food_product
        self.nature.data = spot.nature
        self.views.data = spot.views
        self.experience.data = spot.experience
        self.opentime.data = spot.opentime
        self.closetime.data = spot.closetime

    def copy_to(self, spot):
        spot.area = self.area.data
        spot.cityname = self.cityname.data
        spot.spotname = self.spotname.data
        spot.datetime = self.datetime.data
        spot.latitude = self.latitude.data
        spot.longitude = self.longitude.data
        spot.url = self.url.data
        spot.picture = self.picture.data
        spot.history_culture = self.history_culture.data
        spot.food_product = self.food_product.data
        spot.nature = self.nature.data
        spot.views = self.views.data
        spot.experience = self.experience.data
        spot.opentime = self.opentime.data
        spot.closetime = self.closetime.data

class TouristForm(FlaskForm):
    tourist_spots = SelectMultipleField('Tourist Spots', validators=[DataRequired()], coerce=int)

    def __init__(self, *args, **kwargs):
        super(TouristForm, self).__init__(*args, **kwargs)
        self.spot_list = kwargs.get('spot_list', [])
        tourist_spots_list = []
        [tourist_spots_list.append((spot.id, spot.spotname)) for spot in self.spot_list]
        self.tourist_spots.choices = tourist_spots_list

    cancel = ButtonField("Cancel")
    submit = SubmitField("Submit")
