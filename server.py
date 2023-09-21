from sanic import Sanic,text,Blueprint
from peewee import SqliteDatabase
from services.auth import auth_bp
from services.profiles import profile_bp
from models import *


async def hello(request):
    return text("Welcome to app")


def create_app():
    #Initialize the app
    app = Sanic("conduit")
    # Baseline route when the front end SPA gets added
    app.add_route(hello,"/") 

    #Initialize the database
    db = SqliteDatabase("conduit.db")
    db.create_tables(models=[User.User,Followers.Followers])
    #Make the api blueprint here
    api = Blueprint.group(auth_bp,profile_bp,url_prefix="/api")
    app.blueprint(api)
    
    return app



