from flask import Flask, jsonify
from flask_cors import CORS
import logging
import os

from db_sqlserver import init_sqlserver
# from models import db

# Controllers có sẵn
from controllers.appointment_controller import appointment_bp

# Controllers mới/hoàn thiện
from controllers.auth_controller import auth_bp
from controllers.report_controller import report_bp

# Public Controller (optional)
try:
    from controllers.public_controller import public_bp
except ImportError:
    public_bp = None

# Scheduler (tạm thời comment nếu chưa có)
# from utils.scheduler import start_scheduler


def create_app():
    app = Flask(__name__)
    app.config.setdefault("SECRET_KEY", os.environ.get("SECRET_KEY", "dev_secret_key"))
    app.config.setdefault("JSON_AS_ASCII", False)

    # CORS
    CORS(app)

    # Logging
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="system.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("🚀 Flask app started")

    # DB
    init_sqlserver(app)

    # Register Blueprints
    app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(report_bp, url_prefix="/api/reports")

    if public_bp:
        app.register_blueprint(public_bp, url_prefix="/api/public")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
