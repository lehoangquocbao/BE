# 📘 HIV Treatment and Medical Services System – API List

## 🧑‍⚕️ Người dùng
- `POST /api/auth/register` – Đăng ký tài khoản người dùng
- `POST /api/auth/login` – Đăng nhập
- `GET /api/users` – Lấy danh sách người dùng
- `GET /api/users/:id` – Lấy thông tin người dùng
- `PUT /api/users/:id` – Cập nhật thông tin người dùng
- `DELETE /api/users/:id` – Xóa người dùng

## 📅 Lịch hẹn khám
- `POST /api/appointments` – Đặt lịch khám
- `GET /api/appointments` – Lấy danh sách lịch hẹn
- `GET /api/appointments/:id` – Chi tiết lịch hẹn
- `PUT /api/appointments/:id` – Cập nhật lịch hẹn
- `DELETE /api/appointments/:id` – Hủy lịch hẹn

## 🧪 Xét nghiệm HIV (ARV, CD4, tải lượng...)
- `POST /api/test-results` – Thêm kết quả xét nghiệm
- `GET /api/test-results` – Lấy tất cả kết quả
- `GET /api/test-results/:id` – Chi tiết kết quả
- `PUT /api/test-results/:id` – Cập nhật kết quả

## 💊 Phác đồ điều trị ARV
- `POST /api/treatments` – Tạo phác đồ điều trị
- `GET /api/treatments` – Danh sách phác đồ
- `GET /api/treatments/:id` – Chi tiết phác đồ
- `PUT /api/treatments/:id` – Cập nhật phác đồ

## 🩺 Bác sĩ & lịch làm việc
- `POST /api/doctors` – Tạo bác sĩ
- `GET /api/doctors` – Danh sách bác sĩ
- `GET /api/doctors/:id` – Thông tin bác sĩ
- `POST /api/schedules` – Tạo lịch làm việc bác sĩ
- `GET /api/schedules/:doctorId` – Lịch làm việc theo bác sĩ

## 📞 Tư vấn trực tuyến
- `POST /api/consultations` – Tạo phiên tư vấn
- `GET /api/consultations` – Danh sách tư vấn
- `PUT /api/consultations/:id` – Cập nhật tư vấn

## 🔔 Thông báo nhắc lịch uống thuốc, tái khám
- `POST /api/notifications` – Tạo thông báo
- `GET /api/notifications` – Danh sách thông báo
- `PUT /api/notifications/:id/read` – Đánh dấu đã đọc

## 📊 Dashboard & báo cáo
- `GET /api/reports/summary` – Tổng quan điều trị
- `GET /api/reports/by-treatment` – Báo cáo theo phác đồ
- `GET /api/reports/by-doctor` – Báo cáo theo bác sĩ

---

## 📈 Sơ đồ API (Mermaid)

```mermaid
flowchart TD
    A[Auth] -->|POST| B[Register]
    A -->|POST| C[Login]

    D[Users] -->|GET| E[Danh sách]
    E -->|GET| F[Chi tiết người dùng]
    F -->|PUT| G[Cập nhật]
    G -->|DELETE| H[Xóa]

    I[Lịch hẹn] -->|POST| J[Đặt lịch]
    I -->|GET| K[Xem lịch]

    L[Xét nghiệm] -->|POST| M[Thêm]
    L -->|GET| N[Xem kết quả]

    O[Điều trị] -->|POST| P[Tạo]
    O -->|GET| Q[Xem phác đồ]

    R[Bác sĩ] -->|POST| S[Tạo bác sĩ]
    R -->|GET| T[Xem bác sĩ]
    T -->|GET| U[Lịch làm việc]

    V[Tư vấn] -->|POST| W[Tạo]
    V -->|GET| X[Danh sách]

    Y[Thông báo] -->|POST| Z[Tạo thông báo]
    Y -->|GET| ZA[Danh sách]

    BB[Dashboard] -->|GET| BC[Tổng hợp]
