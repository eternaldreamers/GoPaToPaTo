from flask import Blueprint, request, jsonify
import database.mongo_setup as mongo_setup

cv_routes = Blueprint('cv_routes', __name__)

cv_collection = mongo_setup.database.cvs

@cv_routes.route('/cv', methods=['GET'])
def get_cv():
    return jsonify({"message": "getting uwu bomb"})

@cv_routes.route('/cv', methods=['POST'])
def add_or_update_cv():
    return jsonify({"message": "CV creado con éxito."})

@cv_routes.route('/cv/<cv_id>', methods=['DELETE'])
def delete_cv(cv_id):
    return jsonify({"message": "eliminado con éxito."})
