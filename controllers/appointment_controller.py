from flask import Blueprint, request, jsonify
from models import db
from models.class_appointment import Appointment, Reminder
from datetime import datetime
from utils.validation import require_fields
from utils.security import token_required, roles_required
from models.user import Role

appointment_bp = Blueprint('appointment', __name__)

# Đặt lịch hẹn (cho phép ẩn danh nếu không có user_id)
@appointment_bp.route('/appointments', methods=['POST'])
@token_required
def create_appointment():
    data = request.get_json(force=True, silent=True) or {}
    err = require_fields(data, ["doctor_id", "appointment_time"])
    if err: return err

    user_id = getattr(request, "user", None).id if getattr(request, "user", None) else data.get("user_id")
    doctor_id = data["doctor_id"]
    notes = data.get("notes")

    # Parse datetime
    try:
        appointment_dt = datetime.fromisoformat(data["appointment_time"])
    except Exception:
        return jsonify({"error": "Invalid appointment_time, use YYYY-MM-DDTHH:MM"}), 400

    appt = Appointment(
        user_id=user_id,
        doctor_id=doctor_id,
        appointment_time=appointment_dt,
        notes=notes,
        status="pending"
    )
    db.session.add(appt)
    db.session.commit()
    return jsonify({"message": "Appointment created", "id": appt.id}), 201


# Lấy tất cả lịch hẹn (chỉ Staff/Doctor/Admin)
@appointment_bp.route('/appointments', methods=['GET'])
@roles_required(Role.STAFF, Role.DOCTOR, Role.MANAGER, Role.ADMIN)
def get_appointments():
    appointments = Appointment.query.all()
    result = [{
        'id': a.id,
        'user_id': a.user_id,
        'doctor_id': a.doctor_id,
        'appointment_time': a.appointment_time.isoformat(),
        'status': a.status,
        'notes': a.notes
    } for a in appointments]
    return jsonify(result)


# Lấy chi tiết lịch hẹn (chính chủ hoặc Doctor xem)
@appointment_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
@token_required
def get_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    user = getattr(request, "user", None)

    if user.role not in [Role.DOCTOR, Role.STAFF, Role.MANAGER, Role.ADMIN] and a.user_id != user.id:
        return jsonify({"error": "Forbidden"}), 403

    return jsonify({
        'id': a.id,
        'user_id': a.user_id,
        'doctor_id': a.doctor_id,
        'appointment_time': a.appointment_time.isoformat(),
        'status': a.status,
        'notes': a.notes
    })


# Xác nhận lịch hẹn (chỉ Doctor/Staff/Admin)
@appointment_bp.route('/appointments/<int:appointment_id>/confirm', methods=['PUT'])
@roles_required(Role.DOCTOR, Role.STAFF, Role.ADMIN)
def confirm_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    a.status = 'confirmed'
    db.session.commit()
    return jsonify({'message': 'Appointment confirmed'})


# Hủy lịch hẹn (chính chủ hoặc Admin)
@appointment_bp.route('/appointments/<int:appointment_id>', methods=['DELETE'])
@token_required
def delete_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    user = getattr(request, "user", None)

    if user.role != Role.ADMIN and a.user_id != user.id:
        return jsonify({"error": "Forbidden"}), 403

    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted'})


# Gửi nhắc nhở tái khám, uống thuốc (chỉ Staff/Doctor/Admin)
@appointment_bp.route('/reminders', methods=['POST'])
@roles_required(Role.STAFF, Role.DOCTOR, Role.ADMIN)
def create_reminder():
    data = request.get_json(force=True, silent=True) or {}
    err = require_fields(data, ["appointment_id", "reminder_time", "reminder_type"])
    if err: return err

    appointment = Appointment.query.get(data["appointment_id"])
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404

    try:
        reminder_dt = datetime.fromisoformat(data["reminder_time"])
    except Exception:
        return jsonify({"error": "Invalid reminder_time format, use YYYY-MM-DDTHH:MM"}), 400

    r = Reminder(
        appointment_id=appointment.id,
        reminder_time=reminder_dt,
        reminder_type=data["reminder_type"]
    )
    db.session.add(r)
    db.session.commit()
    return jsonify({'message': 'Reminder created', 'id': r.id}), 201
