from flask import Blueprint, request, jsonify
from models import db, Doctor
from flask_jwt_extended import jwt_required

doctor_bp = Blueprint("doctors", __name__)

# ----------------------
# Lấy danh sách bác sĩ
# ----------------------
@doctor_bp.route("/", methods=["GET"])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "specialty": d.specialty,
            "degree": d.degree,
            "work_schedule": d.work_schedule,
            "email": d.email,
            "phone": d.phone
        } for d in doctors
    ])


# ----------------------
# Thêm bác sĩ mới
# ----------------------
@doctor_bp.route("/", methods=["POST"])
@jwt_required()
def create_doctor():
    data = request.get_json()
    new_doctor = Doctor(
        name=data.get("name"),
        specialty=data.get("specialty"),
        degree=data.get("degree", ""),
        work_schedule=data.get("work_schedule", ""),
        email=data.get("email", ""),
        phone=data.get("phone", "")
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"msg": "Doctor created successfully", "id": new_doctor.id}), 201


# ----------------------
# Lấy lịch làm việc của bác sĩ
# ----------------------
@doctor_bp.route("/<int:doctor_id>/schedule", methods=["GET"])
def get_doctor_schedule(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return jsonify({
        "doctor_id": doctor.id,
        "name": doctor.name,
        "work_schedule": doctor.work_schedule
    })