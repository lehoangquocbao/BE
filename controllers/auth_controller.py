from flask import Blueprint, request, jsonify
from models import db
from models.class_appointment import User, Role
from utils.validation import require_fields
from utils.security import hash_password, verify_password, generate_token, token_required, roles_required

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.get_json(force=True, silent=True) or {}
    err = require_fields(data, ["username", "password"])
    if err: return err

    username = data["username"].strip()
    if db.session.query(User).filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    # kiểm tra role hợp lệ, nếu không thì gán mặc định CUSTOMER
    role = Role(data.get("role")) if data.get("role") in [r.value for r in Role] else Role.CUSTOMER

    user = User(
        username=username,
        email=data.get("email"),
        full_name=data.get("full_name"),
        password_hash=hash_password(data["password"]),
        role=role
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered", "user": user.to_safe_dict()}), 201

@auth_bp.post("/login")
def login():
    data = request.get_json(force=True, silent=True) or {}
    err = require_fields(data, ["username", "password"])
    if err: return err

    user = db.session.query(User).filter_by(username=data["username"]).first()
    if not user or not verify_password(user.password_hash, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user)
    return jsonify({"token": token, "user": user.to_safe_dict()})

@auth_bp.get("/me")
@token_required
def me():
    return jsonify({"user": request.user.to_safe_dict()})

# Ví dụ: endpoint chỉ Admin dùng
@auth_bp.get("/admin-only")
@roles_required(Role.ADMIN)
def admin_only():
    return jsonify({"message": "Hello Admin"})
