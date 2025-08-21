from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, EducationMaterial  # giả định có model EducationMaterial

public_bp = Blueprint("public_bp", __name__)

# DELETE /education/:id
@public_bp.route("/education/<int:education_id>", methods=["DELETE"])
@jwt_required()
def delete_education(education_id):
    edu = EducationMaterial.query.get(education_id)
    if not edu:
        return jsonify({"msg": "Education material not found"}), 404
    
    db.session.delete(edu)
    db.session.commit()
    return jsonify({"msg": "Education material deleted successfully"}), 200
