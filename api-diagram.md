# API List - HIV Treatment and Medical Services System

## Auth (Xác thực người dùng)
POST   /api/auth/register           → Đăng ký tài khoản người dùng  
POST   /api/auth/login              → Đăng nhập hệ thống  

## Quản lý người dùng
GET    /api/users                   → Lấy danh sách người dùng  
GET    /api/users/:id               → Lấy thông tin người dùng theo ID  
PUT    /api/users/:id               → Cập nhật thông tin người dùng  
DELETE /api/users/:id               → Xóa người dùng  

## Đặt lịch khám và điều trị
POST   /api/appointments            → Đặt lịch khám và điều trị HIV  
GET    /api/appointments            → Xem danh sách lịch hẹn  
GET    /api/appointments/:id        → Xem chi tiết lịch hẹn  
PUT    /api/appointments/:id        → Cập nhật lịch hẹn  
DELETE /api/appointments/:id        → Hủy lịch hẹn  

## Kết quả xét nghiệm (ARV, CD4, tải lượng HIV)
POST   /api/test-results            → Thêm kết quả xét nghiệm  
GET    /api/test-results            → Lấy danh sách kết quả xét nghiệm  
GET    /api/test-results/:id        → Lấy chi tiết kết quả xét nghiệm  
PUT    /api/test-results/:id        → Cập nhật kết quả xét nghiệm  

## Quản lý phác đồ điều trị
POST   /api/treatments              → Thêm phác đồ điều trị HIV (VD: TDF + 3TC + DTG)  
GET    /api/treatments              → Xem danh sách phác đồ  
GET    /api/treatments/:id          → Xem chi tiết phác đồ điều trị  
PUT    /api/treatments/:id          → Cập nhật phác đồ điều trị  

## Quản lý bác sĩ
POST   /api/doctors                 → Thêm bác sĩ  
GET    /api/doctors                 → Xem danh sách bác sĩ  
GET    /api/doctors/:id             → Thông tin chi tiết bác sĩ  

## Lịch làm việc bác sĩ
POST   /api/schedules               → Tạo lịch làm việc của bác sĩ  
GET    /api/schedules/:doctorId     → Xem lịch làm việc theo bác sĩ  

## Hỗ trợ tư vấn - đặt lịch trực tuyến
POST   /api/consultations           → Gửi yêu cầu tư vấn  
GET    /api/consultations           → Xem danh sách yêu cầu tư vấn  
PUT    /api/consultations/:id       → Cập nhật trạng thái tư vấn  

## Thông báo (nhắc lịch, cập nhật kết quả, tư vấn,…)
POST   /api/notifications           → Gửi thông báo  
GET    /api/notifications           → Danh sách thông báo  
PUT    /api/notifications/:id/read  → Đánh dấu thông báo đã đọc  

## Báo cáo & Thống kê
GET    /api/reports/summary         → Báo cáo tổng hợp tình hình điều trị  
GET    /api/reports/by-treatment    → Báo cáo theo từng phác đồ điều trị  
GET    /api/reports/by-doctor       → Báo cáo hiệu quả theo bác sĩ  
