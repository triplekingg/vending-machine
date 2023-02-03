from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import certifi
import json

# Initialize Mongodb Database Here
ca = certifi.where()
connection_string = (
    "mongodb+srv://manitG:blah@swe.hqdmzg5.mongodb.net/?retryWrites=true&w=majority"
)
client = MongoClient(connection_string, tlsCaFile=ca)
vending_db = client.Vending
collections = vending_db.list_collection_names()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "blahhh"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Uncomment below to initialize the dummy data into the database
    # initializeVengingMachines()

    return app


def initializeVengingMachines():
    collection = vending_db.vending_machines
    with open("website/data.json") as file:
        test_document = json.load(file)
    collection.insert_many(test_document)
