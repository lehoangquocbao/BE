# BE
BE dự án CNPM (flaskAPI Pyhthon)
Backend Dev 2: API đặt lịch hẹn & Nhắc nhở
Các chức năng:
- Đặt lịch hẹn
- Hủy và xác nhận lịch hẹn 
- Gửi nhắc nhở tái khám và uống thuốc
- Hỗ trợ đặt lịch ẩn danh bằng JWT token đặc biêyj

Ngôn ngữ: Python
Database: SQlite
Khung: Flask

Các thư mục:
BE-1/
├── models/
│ └── class_appointment.py # Lớp Appointment
├── appointment_service.py # API /appointment
├── token_anonymous.py # Xử lý token ẩn danh
├── db_connection.py # Hàm kết nối database
├── test_appointment_post.py # Test API (tùy chọn)
├── app.py # Chạy Flask app
└── README.md # Tài liệu mô tả