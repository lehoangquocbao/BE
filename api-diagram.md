## 🔐 Xác thực & người dùng
| Phương thức | Endpoint                  | Mô tả chức năng                               | Vai trò           |
|------------|----------------------------|-----------------------------------------------|-------------------|
| POST       | /auth/register             | Đăng ký tài khoản                              | Guest             |
| POST       | /auth/login                | Đăng nhập                                      | Guest             |
| GET        | /users/me                  | Lấy thông tin người dùng hiện tại              | Customer, Staff   |
| PUT        | /users/me                  | Cập nhật thông tin cá nhân                     | Customer          |

---

## 🏥 Cơ sở & nội dung công khai
| Phương thức | Endpoint                  | Mô tả chức năng                                | Vai trò          |
|------------|----------------------------|------------------------------------------------|------------------|
| GET        | /info/hospital             | Danh sách cơ sở y tế                           | Guest            |
| GET        | /info/blogs                | Danh sách bài viết chia sẻ, kinh nghiệm        | Guest            |
| GET        | /info/education            | Tài liệu giáo dục & phòng ngừa HIV             | Guest            |

---

## 📆 Đặt lịch khám & lịch hẹn
| Phương thức | Endpoint                       | Mô tả chức năng                          | Vai trò          |
|------------|----------------------------------|------------------------------------------|------------------|
| GET        | /appointments                    | Lịch hẹn của người dùng                  | Customer         |
| POST       | /appointments                    | Đặt lịch hẹn khám với bác sĩ             | Customer         |
| PUT        | /appointments/:id/cancel         | Hủy lịch hẹn                             | Customer         |
| GET        | /appointments/all                | Xem toàn bộ lịch hẹn của bệnh nhân       | Staff, Doctor    |

---

## 🧪 Xét nghiệm & chẩn đoán
| Phương thức | Endpoint                            | Mô tả chức năng                          | Vai trò          |
|------------|---------------------------------------|------------------------------------------|------------------|
| GET        | /patients/:id/tests                   | Xem kết quả xét nghiệm (ARV, CD4,...)    | Customer, Doctor |
| POST       | /patients/:id/tests                   | Nhập kết quả xét nghiệm mới              | Staff            |

---

## 💊 Phác đồ điều trị & thuốc
| Phương thức | Endpoint                          | Mô tả chức năng                              | Vai trò        |
|------------|-------------------------------------|----------------------------------------------|----------------|
| GET        | /patients/:id/treatment             | Xem phác đồ điều trị                         | Customer       |
| POST       | /patients/:id/treatment             | Chỉ định/tùy chỉnh phác đồ                   | Doctor         |
| GET        | /drugs                              | Danh sách thuốc ARV                          | Staff, Doctor  |

---

## 👨‍⚕️ Quản lý bác sĩ & nhân sự
| Phương thức | Endpoint                  | Mô tả chức năng                                | Vai trò      |
|------------|----------------------------|------------------------------------------------|--------------|
| GET        | /doctors                   | Danh sách bác sĩ                               | Manager      |
| POST       | /doctors                   | Thêm bác sĩ mới                                | Admin        |
| GET        | /doctors/:id/schedule      | Lịch làm việc bác sĩ                           | Doctor       |

---

## 📊 Dashboard & báo cáo
| Phương thức | Endpoint                   | Mô tả chức năng                              | Vai trò       |
|------------|-----------------------------|----------------------------------------------|---------------|
| GET        | /dashboard/overview         | Thống kê tổng quan toàn hệ thống             | Admin, Manager|
| GET        | /reports/patients           | Báo cáo theo bệnh nhân                        | Manager       |
| GET        | /reports/treatments         | Báo cáo theo phác đồ điều trị                 | Admin         |

---

## 🗂️ Quản trị hệ thống
| Phương thức | Endpoint                   | Mô tả chức năng                              | Vai trò       |
|------------|-----------------------------|----------------------------------------------|---------------|
| GET        | /users                      | Danh sách toàn bộ người dùng                 | Admin         |
| POST       | /users/:id/assign-role      | Gán quyền cho người dùng                     | Admin         |
| GET        | /config/system              | Lấy cấu hình hệ thống                        | Admin         |
