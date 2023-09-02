from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes.cv_routes import cv_routes
import database.mongo_setup as mongo_setup

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify(message="API de CV en funcionamiento")

app.register_blueprint(cv_routes, url_prefix="/cv")

if __name__ == "__main__":
    mongo_setup.init_db()
    app.run(debug=True)
