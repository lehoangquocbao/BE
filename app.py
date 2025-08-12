
from flask import Flask
from models.class_appointment import db
from db_sqlserver import init_sqlserver
from appointment_api import appointment_bp

app = Flask(__name__)
init_sqlserver(app)
app.register_blueprint(appointment_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)