from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv
from reactpy import component, html
from reactpy.backend.flask import configure, Options
from reactpy_router import route, simple
from frontend.components import PageHome, PageForm, PageProfile

load_dotenv()

app = Flask(__name__)
CORS(app)

cv_routes = Blueprint('cv_routes', __name__)

@component
def root():
    return simple.router(
        route("/home", PageHome()),
        route("/profile", PageProfile()),
        route("/form", PageForm()),
    )

configure(app, root)

@cv_routes.route('/cv', methods=['GET'])
def get_cv():
    return jsonify({"message": "getting uwu bomb"})

app.register_blueprint(cv_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
