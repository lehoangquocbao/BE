from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_anonymous = db.Column(db.Boolean, default=False)
    # appointments = db.relationship('Appointment', backref='user', lazy=True)  # Đã có backref ở Appointment

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # appointments = db.relationship('Appointment', backref='doctor', lazy=True)  # Đã có backref ở Appointment

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'), nullable=True) #nullable=True hỗ trợ ẩn danh anonymous
    doctor_id=db.Column(db.Integer,db.ForeignKey('doctors.id'), nullable=False)
    appointment_time=db.Column(db.DateTime, nullable=False)
    status=db.Column(db.String(20), default='pending')
    notes=db.Column(db.Text, nullable=True)
    created_at=db.Column(db.DateTime, default=datetime.utcnow) # neu khong có time lấy time hiên tại

    user= db.relationship('User', backref='appointments', lazy=True)
    doctor= db.relationship('Doctor', backref='appointments', lazy=True) # thiết lập quan hệ 2 bảng
class reminder(db.Model):
    __tablename__ = 'reminders'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_id=db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    reminder_time=db.Column(db.DateTime, nullable=False)
    reminder_type=db.Column(db.String(50), nullable=False)  # e.g., 'email', 'SMS'
    sent_status=db.Column(db.Boolean, default=False)  # True if reminder has been sent
    appointment=db.relationship('Appointment', backref='reminders', lazy=True)  # thiết lập quan hệ với bảng Appointment

class AnonymousToken(db.Model):
    __tablename__ = 'anonymous_tokens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(64), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
