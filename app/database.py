from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

pyMongoDb = None

def inti_app(app: Flask):
    app.config.from_object(Config)
    global pyMongoDb
    pyMongoDb = PyMongo(app)
    print(pyMongoDb)


def get_pyMongoDb():
    
    return pyMongoDb    
    