from models.class_appointment import db

# Hàm khởi tạo kết nối SQL Server cho Flask app
# Sử dụng trong app.py hoặc main entrypoint

def init_sqlserver(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:Aa123456@127.0.0.1:1433/master?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

# Thay <username>, <password>, <server>, <database> bằng thông tin thực tế của bạn.
# Ví dụ:
# 'mssql+pyodbc://sa:yourpassword@localhost/clinicdb?driver=ODBC+Driver+17+for+SQL+Server'