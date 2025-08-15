from flask import Blueprint, request, jsonify
from models.class_appointment import db, Appointment, Reminder  # ✅ Đúng tên class
from datetime import datetime

appointment_bp = Blueprint('appointment', __name__)

# Đặt lịch hẹn mới (bao gồm cả ẩn danh)
@appointment_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    user_id = data.get('user_id')
    doctor_id = data.get('doctor_id')
    appointment_time = data.get('appointment_time')
    notes = data.get('notes')

    if not doctor_id or not appointment_time:
        return jsonify({'error': 'doctor_id and appointment_time are required'}), 400

    try:
        appointment_dt = datetime.fromisoformat(appointment_time)
    except ValueError:
        return jsonify({'error': 'Invalid appointment_time format, use YYYY-MM-DDTHH:MM'}), 400

    appointment = Appointment(
        user_id=user_id,
        doctor_id=doctor_id,
        appointment_time=appointment_dt,
        notes=notes
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created', 'id': appointment.id}), 201


# Lấy danh sách lịch hẹn
@appointment_bp.route('/appointments', methods=['GET'])
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


# Lấy chi tiết lịch hẹn
@appointment_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    return jsonify({
        'id': a.id,
        'user_id': a.user_id,
        'doctor_id': a.doctor_id,
        'appointment_time': a.appointment_time.isoformat(),
        'status': a.status,
        'notes': a.notes
    })


# Xác nhận lịch hẹn
@appointment_bp.route('/appointments/<int:appointment_id>/confirm', methods=['PUT'])
def confirm_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    a.status = 'confirmed'
    db.session.commit()
    return jsonify({'message': 'Appointment confirmed'})


# Hủy lịch hẹn
@appointment_bp.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    a = Appointment.query.get_or_404(appointment_id)
    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'Appointment deleted'})


# Gửi nhắc nhở tái khám, uống thuốc
@appointment_bp.route('/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()
    appointment_id = data.get('appointment_id')
    reminder_time = data.get('reminder_time')
    reminder_type = data.get('reminder_type')

    if not appointment_id or not reminder_time or not reminder_type:
        return jsonify({'error': 'appointment_id, reminder_time, reminder_type are required'}), 400

    try:
        reminder_dt = datetime.fromisoformat(reminder_time)
    except ValueError:
        return jsonify({'error': 'Invalid reminder_time format, use YYYY-MM-DDTHH:MM'}), 400

    r = Reminder(
        appointment_id=appointment_id,
        reminder_time=reminder_dt,
        reminder_type=reminder_type
    )
    db.session.add(r)
    db.session.commit()
    return jsonify({'message': 'Reminder created', 'id': r.id}), 201
