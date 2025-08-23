from flask import Blueprint, request, jsonify

reminder_bp = Blueprint('reminder_bp', __name__)

@reminder_bp.route('/reminders/<int:id>', methods=['PUT'])
def update_reminder(id):
    data = request.json
    return jsonify({"message": f"Reminder {id} updated", "data": data})

@reminder_bp.route('/reminders/<int:id>', methods=['DELETE'])
def delete_reminder(id):
    return jsonify({"message": f"Reminder {id} deleted"})