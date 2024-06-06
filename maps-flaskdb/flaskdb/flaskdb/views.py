from flask import Blueprint, request, Response, session, render_template, redirect, flash, url_for, jsonify
views = Blueprint("views", __name__, template_folder="templates", static_folder="static")

from flaskdb import app
from flaskdb import util
from flaskdb.models import *
from flaskdb.forms import *
from flaskdb.dataaccess import DataAccess
from flaskdb.ai import GA

import datetime
import pickle
from flask_cachecontrol import dont_cache
from werkzeug.utils import secure_filename
import datetime
import pickle
import pandas as pd
import folium
from folium import plugins
import os
import csv
import pathlib
import imghdr
from PIL import Image

basedir = os.path.dirname(__file__)

@views.route("/", methods=["GET", "POST"])
def index():
    if not "username" in session:
        return redirect(url_for("views.login"))

    return render_template("index.html")

@views.route("/now", methods=["GET", "POST"])
def now():
    return str(datetime.datetime.now())

@views.route("/initdb", methods=["GET", "POST"])
def initdb():
    db.drop_all()
    db.create_all()
    
    admin = User(username="admin", password="password")
    user = User(username="user", password="password")
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    return "initidb() method was executed. "

@views.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        da = DataAccess(app)
        user = da.auth(form.username.data, form.password.data)
        if user is None:
            flash("Username or Password is incorrect.", "danger")
            return redirect(url_for("views.login"))

        session["username"] = user.username
        return redirect(url_for("views.index"))
    return render_template("login.html", form=form)

@views.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None)
    session.clear()
    return redirect(url_for("views.index"))

@views.route("/dataset", methods=["GET", "POST"])
@dont_cache()
def dataset():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    da = DataAccess(app)
    spotlist = da.get_spots()
    res = ""
    for s in spotlist:
        res += f"  [{s.id}, {s.user_id}, {s.area}, {s.cityname}, {s.spotname}, \
{s.datetime}, {s.latitude}, {s.longitude}, {s.url}, {s.picture}, \
{s.history_culture}, {s.food_product}, {s.nature}, {s.views}, \
{s.experience}, {s.opentime}, {s.closetime}],\n"

    res = '[\n' + res + ']'
    return Response(res, mimetype="text/plain")

@views.route("/upload", methods=["GET", "POST"])
@dont_cache()
def upload():
    print("upload")
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    form = SpotForm()
    if form.validate_on_submit():
        print("submit")

        area = form.area.data
        cityname = form.cityname.data
        spotname = form.spotname.data
        file = form.picture.data

        suffix = pathlib.Path(file.filename).suffix
        if not suffix in app.config["ALLOWED_EXTENSIONS"]:
            return "not allowed extension : {}".format(suffix)

        file_type = imghdr.what(file.stream)
        if not file_type in app.config["ALLOWED_TYPES"]:
            return "not allowed file type : {}".format(file_type)

        filepath = os.path.join(basedir, app.config["FILE_UPLOAD_DIR"] + secure_filename(file.filename))
        file.save(filepath)
        im = Image.open(filepath)
        datetime = util.extract_datetime(im)
        latitude, longitude = util.extract_geocode(im)
        url = form.url.data

        da = DataAccess(app)
        user_id = da.get_user_id(session["username"])
        spot = [user_id, area, cityname, spotname, datetime, float(latitude), float(longitude), url, filepath]
        da.add_spot(spot)

        spotlist = [str(s) for s in spot]
        return Response(",".join(spotlist), mimetype="text/plain")
    return render_template("upload.html", form=form)


@views.route("/maps/<string:name>/", methods=["GET", "POST"])
@dont_cache()
def maps(name):
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    da = DataAccess(app)
    if name == "all":
        spotlist = da.get_spots()
        maps = folium.Map(location=[3.5, 31.6], zoom_start=2)
    elif name == "newyork":
        spotlist = da.get_spots_by_area("newyork")
        maps = folium.Map(location=[40.7387, -73.9925], zoom_start=13)
    elif name == "london":
        spotlist = da.get_spots_by_area("london")
        maps = folium.Map(location=[51.50733, -0.12763], zoom_start=11)
    elif name == "tokyo":
        spotlist = da.get_spots_by_area("tokyo")
        maps = folium.Map(location=[35.6645,139.7104], zoom_start=11)
    elif name == "spring":
        spotlist = da.get_spots_by_season("2020-01-01", "2020-04-01")
        maps = folium.Map(location=[35.6645,139.7104], zoom_start=11)
    elif name == "autumn":
        spotlist = da.get_spots_by_season("2020-07-01", "2020-10-01")
        maps = folium.Map(location=[35.6645,139.7104], zoom_start=11)
    else:
        maps = folium.Map(location=[3.5, 31.6], zoom_start=2)
    for spot in spotlist:
        if spot.picture is not None and spot.picture != "":
            index = spot.picture.rfind("/")
            filename = spot.picture[index + 1:]
            if spot.picture.startswith("http://") or spot.picture.startswith("https://"):
                popup_content = spot.spotname + '<br><img src="' + spot.picture + '" alt="' + filename+ '" height="120">'
            else:
                popup_content = spot.spotname + '<br><img src="../../static/img/' + filename + '" alt="' + filename+ '" height="120">'
        else:
            popup_content = spot.spotname
        folium.Marker(location=[spot.latitude, spot.longitude], popup=popup_content).add_to(maps)

    filepath = os.path.join(basedir, "templates/maps.html")
    maps.save(filepath)
    
    return render_template("maps.html")

@views.route("/maps/<string:lat>/<string:lng>/", methods=["GET", "POST"])
@dont_cache()
def maps_by_latlng(lat, lng):
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    return maps_by_latlng_with_zoom(lat, lng, None)

@views.route("/maps/<string:lat>/<string:lng>/<string:zoom>/", methods=["GET", "POST"])
@dont_cache()
def maps_by_latlng_with_zoom(lat, lng, zoom):
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    if zoom is None:
        zoom = 10
    maps = folium.Map(location=[float(lat), float(lng)], zoom_start=int(zoom))
    folium.Marker(location=[float(lat), float(lng)], popup="lat: " + lat + ", lng: " + lng).add_to(maps)
    filepath = os.path.join(basedir, "templates/maps.html")
    maps.save(filepath)
    return render_template("maps.html")

@views.route("/searchspot", methods=["GET", "POST"])
@dont_cache()
def searchspot():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    form = SpotForm()
    if form.validate_on_submit():
        da = DataAccess(app)
        spotlist = da.get_spots_by_spotname(form.spotname.data)
        return render_template("search.html", form=form, spotlist=spotlist)
    return render_template("search.html", form=form)

@views.route("/searchspot_ga", methods=["GET", "POST"])
@dont_cache()
def searchspot_ga():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("views.login"))

    da = DataAccess(app)
    spot_list = da.get_spots()

    form = TouristForm(spot_list=spot_list)
    if form.validate_on_submit():
        selected_spots = []
        selected_spots = form.tourist_spots.data
        spot_list = da.get_spots_by_ids(selected_spots)

        ga = GA()
        route, dist = ga.compute(spot_list)

        maps = folium.Map(location=[3.5, 31.6], zoom_start=2)
        line_data1 = []
        [line_data1.append((spot_list[rt].latitude, spot_list[rt].longitude)) for rt in route]

        i = 1
        u = ["st", "nd", "rd", "th"]
        n = 0
        for rt in route:
            if spot_list[rt].picture is not None and spot_list[rt].picture != "":
                index = spot_list[rt].picture.rfind("/")
                filename = spot_list[rt].picture[index + 1:]
                if spot_list[rt].picture.startswith("http://") or spot_list[rt].picture.startswith("https://"):
                    popup_content = """
                        {}{}: {} {}<br><img src=\"{}\" alt=\"{}\" height=\"120\">
                    """.format(
                        i, u[n], spot_list[rt].id, spot_list[rt].spotname, spot_list[rt].picture, filename
                    )
                else:
                    popup_content = """
                        {}{}: {} {}<br><img src=\"../../static/img/{}\" alt=\"{}\" height=\"120\">
                    """.format(
                        i, u[n], spot_list[rt].id, spot_list[rt].spotname, filename, filename
                    )
            else:
                popup_content = """
                    {}{}: {} {}
                """.format(
                    i, u[n], spot_list[rt].id, spot_list[rt].spotname
                )
            folium.Marker(location=[spot_list[rt].latitude, spot_list[rt].longitude], popup=popup_content).add_to(maps)
            i = i + 1
            n = n + 1
            if n > 3:
                n = 3

        line_data1.append(line_data1[0])
        line1 = folium.PolyLine(line_data1, weight=5, color="#FF0000").add_to(maps)
        plugins.PolyLineTextPath(line1, "Total Distance: " + str(dist), offset=-2).add_to(maps)

        filepath = os.path.join(basedir, "templates/maps.html")
        maps.save(filepath)

        return render_template("maps.html")

    return render_template("search_ga.html", form=form)
