import os
import jwt
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, jsonify
from models.user import Role, User
from models import db

# Password helpers
def hash_password(plain: str) -> str:
    return generate_password_hash(plain)

def verify_password(hash_value: str, plain: str) -> bool:
    return check_password_hash(hash_value, plain)

# JWT helpers
def _secret() -> str:
    return (current_app.config.get("SECRET_KEY")
            or os.environ.get("SECRET_KEY")
            or "dev_secret_key")

def generate_token(user: User, expires_hours=8) -> str:
    payload = {
        "sub": user.id,
        "username": user.username,
        "role": user.role.value,
        "exp": datetime.utcnow() + timedelta(hours=expires_hours)
    }
    return jwt.encode(payload, _secret(), algorithm="HS256")

def decode_token(token: str):
    return jwt.decode(token, _secret(), algorithms=["HS256"])

# Decorators
def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing Bearer token"}), 401
        token = auth_header.split(" ", 1)[1].strip()
        try:
            payload = decode_token(token)
            user = db.session.get(User, payload["sub"])
            if not user or not user.is_active:
                return jsonify({"error": "User disabled or not found"}), 401
            request.user = user
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except Exception:
            return jsonify({"error": "Invalid token"}), 401
        return fn(*args, **kwargs)
    return wrapper

def roles_required(*roles: Role):
    allowed = {r.value if isinstance(r, Role) else str(r) for r in roles}
    def decorator(fn):
        @wraps(fn)
        @token_required
        def wrapper(*args, **kwargs):
            user: User = getattr(request, "user", None)
            if not user or user.role.value not in allowed:
                return jsonify({"error": "Forbidden"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
