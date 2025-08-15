from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# --- BE DEV1 ---
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_anonymous = db.Column(db.Boolean, default=False)

class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(50))
    specialty = db.Column(db.String(100))
    work_schedule = db.Column(db.Text)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    medical_records = db.relationship("MedicalRecord", backref="doctor", lazy=True)
    treatment_histories = db.relationship("TreatmentHistory", backref="doctor", lazy=True)
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pending')
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref='appointments', lazy=True)
    reminders = db.relationship('Reminder', backref='appointment', lazy=True)

class Reminder(db.Model):  # <-- CHỮ HOA
    __tablename__ = 'reminders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    reminder_time = db.Column(db.DateTime, nullable=False)
    reminder_type = db.Column(db.String(50), nullable=False)
    sent_status = db.Column(db.Boolean, default=False)

class AnonymousToken(db.Model):
    __tablename__ = 'anonymous_tokens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(64), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

# --- BE DEV2 ---
class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    contact_info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    medical_records = db.relationship("MedicalRecord", backref="patient", lazy=True)
    treatment_histories = db.relationship("TreatmentHistory", backref="patient", lazy=True)

class MedicalRecord(db.Model):
    __tablename__ = "medical_records"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    diagnosis = db.Column(db.Text)
    treatment_plan = db.Column(db.Text)
    notes = db.Column(db.Text)

class ARVProtocol(db.Model):
    __tablename__ = "arv_protocols"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    for_group = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    treatment_histories = db.relationship("TreatmentHistory", backref="arv_protocol", lazy=True)

class TreatmentHistory(db.Model):
    __tablename__ = "treatment_histories"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    arv_protocol_id = db.Column(db.Integer, db.ForeignKey("arv_protocols.id"), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    notes = db.Column(db.Text)
