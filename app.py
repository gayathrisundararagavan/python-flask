from pathlib import Path
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS #used for security purpose protect from hacking process
from flask_pymongo import pymongo
from simple_app.endpoints import project_api_routes


def create_app():
    web_app = Flask(__name__) #Initialising Flask App it is a constructor
    CORS(web_app)  # register webapp in cors

    api_blueprint = Blueprint('api_blueprint',__name__) # creating a copy of same cors standard syntax for flask to create blueprint
    api_blueprint = project_api_routes(api_blueprint)

    web_app.register_blueprint(api_blueprint, url_prefix='/api')
    return web_app

app = create_app()
if __name__ == "__main__":
    app.run()
