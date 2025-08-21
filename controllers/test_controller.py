from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, TestResult, Patient  # giả định có model TestResult

test_bp = Blueprint("test_bp", __name__)

# GET /patients/:id/tests
@test_bp.route("/patients/<int:patient_id>/tests", methods=["GET"])
@jwt_required()
def get_patient_tests(patient_id):
    tests = TestResult.query.filter_by(patient_id=patient_id).all()
    return jsonify([t.as_dict() for t in tests]), 200

# POST /patients/:id/tests
@test_bp.route("/patients/<int:patient_id>/tests", methods=["POST"])
@jwt_required()
def add_patient_test(patient_id):
    data = request.json
    new_test = TestResult(
        patient_id=patient_id,
        test_type=data.get("test_type"),
        result=data.get("result"),
        date=data.get("date")
    )
    db.session.add(new_test)
    db.session.commit()
    return jsonify({"msg": "Test added successfully", "test": new_test.as_dict()}), 201
