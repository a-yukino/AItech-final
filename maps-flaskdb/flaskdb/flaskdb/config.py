# config.py - defines constants values of flaskdb. Modify this if you need.
# Copyright (C) 2024 Yasuhiro Hayashi

import os

CONTEXT_PATH = "/maps-flaskdb"

SECRET_KEY = os.urandom(32)
#SECRET_KEY = CONTEXT_PATH[1:] + "_key" # if secret_key should be stabled.
SESSION_COOKIE_NAME = CONTEXT_PATH[1:] + "_cookie"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False           # if https is enabled, change True
SESSION_COOKIE_SAMESITE = "Lax"
WTF_CSRF_SECRET_KEY = os.urandom(32)
WTF_CSRF_ENABLED = True

DBTYPE   = "postgresql"
HOSTNAME = "127.0.0.1"
PORT     = "5432"
DBNAME   = "maps-flaskdb"
USERNAME = "postgres"
PASSWORD = "c4cf7065b034787b2061088190bf737e"
SHOW_SQL = True

SQLALCHEMY_DATABASE_URI = f"{DBTYPE}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG"]
ALLOWED_TYPES = ["jpeg", "png"]
SPOT_LIST_FILE = "spot_list.csv"
FILE_UPLOAD_DIR = "uploads" + "/"

JSON_AS_ASCII = False
