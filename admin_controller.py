from flask import Blueprint, request, jsonify
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["User A", "User B"]})

@admin_bp.route('/users/<int:id>/assign-role', methods=['POST'])
def assign_role(id):
    role = request.json.get("role")
    return jsonify({"message": f"Assigned role '{role}' to user {id}"})