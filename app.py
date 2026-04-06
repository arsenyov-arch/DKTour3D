from flask import Flask, render_template
from peewee import *

db = SqliteDatabase('instance/dktour.db')

class Kvant(Model):
    name = CharField(32)
    information = TextField()
    coordinates = CharField()

    class Meta:
        database = db


class Place(Model):
    coordinates = CharField()

    class Meta:
        database = db

db.create_tables([Kvant, Place])

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("Home.html")

@app.route("/kvant")
def kvant_page():
    return render_template("KVANT.html")

@app.route("/dzhd")
def dzhd_page():
    return render_template("DZHD.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")