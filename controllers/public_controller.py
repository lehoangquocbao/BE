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


public_bp = Blueprint("public", __name__)

# Mock data (sau có DB thì thay)
hospitals = [
    {"id": 1, "name": "Bệnh viện A", "address": "Hà Nội"},
    {"id": 2, "name": "Bệnh viện B", "address": "TP.HCM"}
]

blogs = [
    {"id": 1, "title": "Blog 1", "content": "Nội dung 1"},
    {"id": 2, "title": "Blog 2", "content": "Nội dung 2"}
]

educations = [
    {"id": 1, "title": "Tài liệu 1", "description": "Mô tả 1"},
    {"id": 2, "title": "Tài liệu 2", "description": "Mô tả 2"}
]

# ========== HOSPITAL ==========
@public_bp.route("/info/hospital", methods=["GET"])
def get_hospital_info():
    return jsonify(hospitals), 200

# ========== BLOGS ==========
@public_bp.route("/info/blogs", methods=["GET"])
def get_blogs():
    return jsonify(blogs), 200

@public_bp.route("/blogs", methods=["POST"])
def create_blog():
    data = request.get_json()
    new_id = len(blogs) + 1
    new_blog = {"id": new_id, "title": data.get("title"), "content": data.get("content")}
    blogs.append(new_blog)
    return jsonify(new_blog), 201

@public_bp.route("/blogs/<int:blog_id>", methods=["PUT"])
def update_blog(blog_id):
    data = request.get_json()
    for blog in blogs:
        if blog["id"] == blog_id:
            blog["title"] = data.get("title", blog["title"])
            blog["content"] = data.get("content", blog["content"])
            return jsonify(blog), 200
    return jsonify({"error": "Blog not found"}), 404

@public_bp.route("/blogs/<int:blog_id>", methods=["DELETE"])
def delete_blog(blog_id):
    for blog in blogs:
        if blog["id"] == blog_id:
            blogs.remove(blog)
            return jsonify({"message": "Deleted successfully"}), 200
    return jsonify({"error": "Blog not found"}), 404

# ========== EDUCATION ==========
@public_bp.route("/info/education", methods=["GET"])
def get_education():
    return jsonify(educations), 200

@public_bp.route("/education", methods=["POST"])
def create_education():
    data = request.get_json()
    new_id = len(educations) + 1
    new_edu = {"id": new_id, "title": data.get("title"), "description": data.get("description")}
    educations.append(new_edu)
    return jsonify(new_edu), 201

@public_bp.route("/education/<int:edu_id>", methods=["PUT"])
def update_education(edu_id):
    data = request.get_json()
    for edu in educations:
        if edu["id"] == edu_id:
            edu["title"] = data.get("title", edu["title"])
            edu["description"] = data.get("description", edu["description"])
            return jsonify(edu), 200
    return jsonify({"error": "Education not found"}), 404
