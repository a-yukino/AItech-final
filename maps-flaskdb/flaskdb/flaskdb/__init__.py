# __init__.py - defines initial conditions of flaskdb
# Copyright (C) 2024 Yasuhiro Hayashi

from flask import Flask

app = Flask(__name__)
app.config.from_object("flaskdb.config")

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_bootstrap import Bootstrap
bs = Bootstrap(app)

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

#from flaskdb.dataaccess import DataAccess
#da = DataAccess(app)

from flaskdb.views import views
app.register_blueprint(views, url_prefix=app.config["CONTEXT_PATH"] + "/")

# from flask import url_for, redirect
# @app.route("/", methods=["GET", "POST"])
# def index():
#     return redirect(url_for("views.login"))
