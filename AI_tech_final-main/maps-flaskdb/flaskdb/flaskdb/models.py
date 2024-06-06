# models.py - defines logical models handling data between a database and the sample web app
# Copyright (C) 2024 Yasuhiro Hayashi

from flaskdb import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id

class Spot(db.Model):
    __tablename__ = "spots"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    area = db.Column(db.String(128), nullable=True)
    cityname = db.Column(db.String(128), nullable=True)
    spotname = db.Column(db.String(128), nullable=True)
    datetime = db.Column(db.DateTime(timezone=True), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    url = db.Column(db.String(128), nullable=True)
    picture = db.Column(db.String(128), nullable=True)
    history_culture = db.Column(db.Integer, nullable=True)
    food_product = db.Column(db.Integer, nullable=True)
    nature = db.Column(db.Integer, nullable=True)
    views = db.Column(db.Integer, nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    opentime = db.Column(db.Time(timezone=True), nullable=True)
    closetime = db.Column(db.Time(timezone=True), nullable=True)

    def __str__(self):
        return "%d, %d" % self.id, self.user_id

    def __repr__(self):
        return "<Spot %r>" % self.id
