from flask import Blueprint, request, jsonify
from models.curriculum import Curriculum

cv_routes = Blueprint('cv_routes', __name__)

@cv_routes.route('/cv', methods=['GET'])
def get_cv():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Se requiere el email para buscar un CV."}), 400
    
    cv = Curriculum.find_by_email(email)
    if cv:
        return jsonify(cv), 200
    else:
        return jsonify({"error": "CV no encontrado."}), 404

@cv_routes.route('/cv', methods=['POST'])
def add_or_update_cv():
    data = request.get_json()
    if not data or not all(k in data for k in ("user_email", "education", "experience", "skills")):
        return jsonify({"error": "Falta información para crear o actualizar el CV."}), 400

    cv = Curriculum(data['user_email'], data['education'], data['experience'], data['skills'])
    cv.save()
    
    return jsonify({"message": "CV creado o actualizado con éxito."}), 201

@cv_routes.route('/cv/<cv_id>', methods=['DELETE'])
def delete_cv(cv_id):
    cv = Curriculum.find_by_email(cv_id)
    if cv:
        Curriculum.delete_by_email(cv_id)
        return jsonify({"message": "CV eliminado con éxito."}), 200
    else:
        return jsonify({"error": "CV no encontrado."}), 404
