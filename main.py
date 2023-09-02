from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from reactpy import component, html
from reactpy.backend.flask import configure
from frontend.routes import cv_routes

app = Flask(__name__)
CORS(app)

load_dotenv()

app.register_blueprint(cv_routes, url_prefix="xd")

configure(app, HelloWorld)