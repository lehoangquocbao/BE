from db_connection import connect_db
from models.class_appointment import appointment
from flask import Blueprint, request, jsonify

appointment_hp=Blueprint('appointment',__name__)
@appointment_hp.route('/appointment', methods=['POST'])
def appointment():
    data=request.get_json()
    appointment=Appointment(
        id=data['id'],
        user_id=data['user_id'],
        doctor_name=data['doctor_name'],
        appointment_time=data['appointment_time'],
        status=data['status']

    )

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (id, user_id, doctor_name, appointment_time, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (appointment.id, appointment.user_id, appointment.doctor_name, appointment.appointment_time, appointment.status))
    conn.commit()
    conn.close()
