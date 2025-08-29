from flask import Blueprint, jsonify, request
from models import db
from models.user import User, Role
from utils.security import roles_required

# Nếu bạn có Appointment, Treatment... import thêm để thống kê
from models.class_appointment import Appointment  # sửa tên theo model của bạn

report_bp = Blueprint("report", __name__)

@report_bp.get("/summary")
@roles_required(Role.MANAGER, Role.ADMIN, Role.STAFF)
def summary():
    # Thống kê đơn giản (có thể tối ưu bằng view/materialized view sau)
    users_total = db.session.query(User).count()
    doctors = db.session.query(User).filter(User.role == Role.DOCTOR).count()
    patients = db.session.query(User).filter(User.role == Role.CUSTOMER).count()
    appts_total = db.session.query(Appointment).count()

    return jsonify({
        "users_total": users_total,
        "doctors": doctors,
        "patients": patients,
        "appointments_total": appts_total
    })

@report_bp.get("/appointments-by-day")
@roles_required(Role.MANAGER, Role.ADMIN, Role.STAFF, Role.DOCTOR)
def appt_by_day():
    # Ví dụ gom theo ngày
    rows = db.session.query(
        db.func.convert(db.String, db.func.cast(Appointment.date, db.Date)),  # SQLServer: CONVERT/CAST tùy driver
        db.func.count()
    ).group_by(
        db.func.convert(db.String, db.func.cast(Appointment.date, db.Date))
    ).all()

    data = [{"date": r[0], "count": r[1]} for r in rows]
    return jsonify({"items": data})
