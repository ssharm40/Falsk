import configparser
from django.template import engines
import sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
config= configparser.ConfigParser()
config.read('src/app_config.ini')

ENV= config.get("DEV", "ENV")
LOCATION = config.get("DEV", "LOCATION")

user_name= config.get("DEV", "user_name")
password= config.get("DEV", "password")
database= config.get("DEV", "database")
host= config.get("DEV", "host")


app= Flask(__name__)
postgres_url= f"""postgresql://{user_name}:{password}@{host}/{database}"""
app.config['SQLALCHEMY_DATABASE_URI']= postgres_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['ENV']= ENV

db=SQLAlchemy(app)
db.app= app
app.app_context().push()

os.environ['ENV']= ENV
os.environ['LOCATION']= LOCATION

SQLALCHEMY_ECHO= False
SQLALCHEMY_TRACK_MODIFICATIONS= True
SQLALCHEMY_DATABASE_URI= app.config['SQLALCHEMY_DATABASE_URI']
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])












