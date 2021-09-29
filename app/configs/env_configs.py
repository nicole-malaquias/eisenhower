from dotenv import load_dotenv
from flask import Flask
from os import environ

load_dotenv()

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(environ.get('SQLALCHEMY_TRACK_MODIFIC'))
    app.config['JSON_SORT_KEYS'] = False
