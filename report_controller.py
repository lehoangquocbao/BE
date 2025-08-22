from flask import Blueprint, jsonify

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/dashboard/overview', methods=['GET'])
def dashboard_overview():
    return jsonify({"overview": "System stats here"})

@report_bp.route('/reports/patients', methods=['GET'])
def report_patients():
    return jsonify({"report": "Patient report data"})

@report_bp.route('/reports/treatments', methods=['GET'])
def report_treatments():
    return jsonify({"report": "Treatment report data"})