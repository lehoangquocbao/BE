from db_connection import connect_db
from models.appointment import Appointment

def insert_appointment(appointment: Appointment):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (id, user_id, doctor_name, appointment_time, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (appointment.id, appointment.user_id, appointment.doctor_name, appointment.appointment_time, appointment.status))
    conn.commit()
    conn.close()
