from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv
from reactpy import component, html
from reactpy.backend.flask import configure, Options
from reactpy_router import route, simple

load_dotenv()

app = Flask(__name__)
CORS(app)

cv_routes = Blueprint('cv_routes', __name__)

# page

@component
def PageHome():
    return html.h1("Home Page!!!!")

@component
def PageProfile():
    return html.h1("profile Page!!!!")

@component
def root():
    return simple.router(
        route("/home", PageHome()),
        route("/profile", PageProfile()),
    )




# # @cv_routes.route('/page', methods=['GET'])
# # def add_or_update_cv():
# #     return jsonify({"message": "CV creado con éxito."})

# opts = Options(
#     # url_prefix='/page',
#     # serve_index_route=False,  # Cambia esto a False si no quieres que se sirva la ruta de índice
#     # cors=True  # Cambia esto a True si quieres habilitar la compatibilidad con CORS
# )
# opts.url_prefix = "/page"


configure(app, root)

@cv_routes.route('/cv', methods=['GET'])
def get_cv():
    return jsonify({"message": "getting uwu bomb"})

app.register_blueprint(cv_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
