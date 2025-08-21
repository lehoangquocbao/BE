from models.class_appointment import db

# Hàm khởi tạo kết nối SQL Server cho Flask app
# Sử dụng trong app.py hoặc main entrypoint

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///be_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Thay <username>, <password>, <server>, <database> bằng thông tin thực tế của bạn.
# Ví dụ:
# 'mssql+pyodbc://sa:yourpassword@localhost/clinicdb?driver=ODBC+Driver+17+for+SQL+Server'