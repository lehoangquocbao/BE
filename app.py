from flask import Flask
from models.class_appointment import db, Appointment, Reminder, AnonymousToken
from db_sqlserver import init_sqlserver
from appointment_api import appointment_bp  # Import blueprint API

app = Flask(__name__)

# Khởi tạo kết nối SQL Server
init_sqlserver(app)

# Đăng ký blueprint API lịch hẹn
app.register_blueprint(appointment_bp)

if __name__ == '__main__':
    with app.app_context():
        # Tạo tất cả bảng trong CSDL nếu chưa có
        db.create_all()
    app.run(debug=True)
