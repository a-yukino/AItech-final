# dataaccess.py - provides data access methods to a relational database. 
# Modify this if you need while referring to the following page to avoid SQL injection 
# https://www.psycopg.org/docs/sql.html
# Copyright (C) 2024 Yasuhiro Hayashi

from psycopg2 import sql, connect, ProgrammingError
from psycopg2.sql import SQL, Identifier, Literal
from flaskdb import app
from flaskdb.models import *

class DataAccess:

    # def __init__(self, hostname, port, dbname, username, password):
    #     self.dburl = "host=" + hostname + " port=" + str(port) + \
    #                  " dbname=" + dbname + " user=" + username + \
    #                  " password=" + password

    def __init__(self, app):
        self.dburl = "host=" + app.config["HOSTNAME"] + " port=" + app.config["PORT"] + \
                     " dbname=" + app.config["DBNAME"] + " user=" + app.config["USERNAME"] + \
                     " password=" + app.config["PASSWORD"]

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))
            conn.autocommit = autocommit
            with conn.cursor() as cur:
                cur.execute(query)
                if not autocommit:
                    conn.commit()
                try:
                    return cur.fetchall()
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    def auth(self, username, password):
        query = SQL("""
            SELECT id, username, password 
            FROM users 
            WHERE username = {username} 
            AND password = {password}
        """).format(
            username = Literal(username),
            password = Literal(password)
        )
        result = self.execute(query, autocommit=True)
        if result:
            user = User()
            user.id = result[0][0]
            user.username = result[0][1]
            return user
        return None

    def get_user_id(self, username):
        query = SQL("""
            SELECT id 
            FROM users 
            WHERE username = {username}
        """).format(
            username = Literal(username)
        )
        result = self.execute(query, autocommit=True)
        if result:
            return result[0][0]
        return None

    def get_spot_by_id(self, id):
        query = SQL("""
            SELECT * 
            FROM spots 
            WHERE id = {id}
        """).format(
            id = Literal(id)
        )
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def get_spots(self):
        query = SQL("""
            SELECT * 
            FROM spots 
        """)
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def get_spots_by_ids(self, ids):
        query = SQL("""
            SELECT *
            FROM spots
            WHERE id IN ({})
        """).format(
            SQL(",").join(map(Literal, ids))
        )
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def get_spots_by_spotname(self, spotname):
        query = SQL("""
            SELECT * 
            FROM spots 
            WHERE spotname LIKE {spotname}
        """).format(
            spotname = Literal("%" + spotname + "%")
        )
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def get_spots_by_area(self, area):
        query = SQL("""
            SELECT * 
            FROM spots 
            WHERE area = {area}
        """).format(
            area = Literal(area)
        )
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def get_spots_by_season(self, frm, too):
        query = SQL("""
            SELECT * 
            FROM spots 
            WHERE datetime >= {frm} 
            AND datetime < {too}
        """).format(
            frm = Literal(frm),
            too = Literal(too)
        )
        result = self.execute(query, autocommit=True)
        if result:
            return self.to_spotlist(result)
        return None

    def to_spotlist(self, result):
        spotlist = []
        for res in result:
            spot = Spot()
            spot.id = res[0]
            spot.user_id = res[1]
            spot.area = res[2]
            spot.cityname = res[3]
            spot.spotname = res[4]
            spot.datetime = res[5]
            spot.latitude = res[6]
            spot.longitude = res[7]
            spot.url = res[8]
            spot.picture = res[9]
            spot.history_culture = res[10]
            spot.food_product = res[11]
            spot.nature = res[12]
            spot.views = res[13]
            spot.experience = res[14]
            spot.opentime = res[15]
            spot.closetime = res[16]
            spotlist.append(spot)
        return spotlist

    def add_spot(self, spot):
        query = SQL("""
            INSERT INTO spots ( {fields} ) 
            VALUES ( {values} )
        """).format(
            fields = SQL(", ").join([
                Identifier("user_id"),
                Identifier("area"),
                Identifier("cityname"),
                Identifier("spotname"),
                Identifier("datetime"),
                Identifier("latitude"),
                Identifier("longitude"),
                Identifier("url"),
                Identifier("picture")
            ]),
            values = SQL(", ").join([
                Literal(spot[0]),
                Literal(spot[1]),
                Literal(spot[2]),
                Literal(spot[3]),
                Literal(spot[4]),
                Literal(spot[5]),
                Literal(spot[6]),
                Literal(spot[7]),
                Literal(spot[8])
            ])
        )
        return self.execute(query, autocommit=True)
