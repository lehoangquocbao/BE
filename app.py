from flask import Flask
from models.class_appointment import db
from appointment_api import appointment_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # hoặc URI phù hợp với bạn
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(appointment_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)