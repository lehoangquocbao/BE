from flask import Flask
from models.class_appointment import db, Appointment, Reminder, AnonymousToken
from db_sqlserver import init_db
from appointment_api import appointment_bp  # Import blueprint API


app = Flask(__name__)

# Route trang chủ tránh lỗi 404
@app.route('/')
def home():
    return "API Backend đang chạy!", 200

# Khởi tạo kết nối database (SQLite mặc định)
init_db(app)

# Đăng ký blueprint API lịch hẹn
app.register_blueprint(appointment_bp)

if __name__ == '__main__':
    with app.app_context():
        # Tạo tất cả bảng trong CSDL nếu chưa có
        db.create_all()
    app.run(debug=True)
from controllers.doctor_controller import doctor_bp
## Đã xóa import và đăng ký blueprint patient_bp vì file không tồn tại

