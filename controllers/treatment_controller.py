from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, TreatmentPlan, Drug

treatment_bp = Blueprint("treatment_bp", __name__)

# GET /patients/:id/treatment
@treatment_bp.route("/patients/<int:patient_id>/treatment", methods=["GET"])
@jwt_required()
def get_treatment(patient_id):
    plan = TreatmentPlan.query.filter_by(patient_id=patient_id).first()
    if not plan:
        return jsonify({"msg": "No treatment plan found"}), 404
    return jsonify(plan.as_dict()), 200

# POST /patients/:id/treatment
@treatment_bp.route("/patients/<int:patient_id>/treatment", methods=["POST"])
@jwt_required()
def add_treatment(patient_id):
    data = request.json
    new_plan = TreatmentPlan(
        patient_id=patient_id,
        regimen=data.get("regimen"),
        start_date=data.get("start_date"),
        notes=data.get("notes")
    )
    db.session.add(new_plan)
    db.session.commit()
    return jsonify({"msg": "Treatment plan created", "treatment": new_plan.as_dict()}), 201

# GET /drugs
@treatment_bp.route("/drugs", methods=["GET"])
@jwt_required()
def get_drugs():
    drugs = Drug.query.all()
    return jsonify([d.as_dict() for d in drugs]), 200
