class User:
    def __init__(self, id, username, email, password, created_at, is_anonymous=False):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_anonymous = is_anonymous # True nếu người dùng là ẩn danh

class Doctor:
    def __init__(self, id, name, degree, specialty, work_schedule, email, phone, created_at):
        self.id = id
        self.name = name
        self.degree = degree              # bằng cấp 
        self.specialty = specialty        # chuyên môn 
        self.work_schedule = work_schedule  # lịch làm việc 
        self.email = email
        self.phone = phone
        self.created_at = created_at

class Appointment:
    def __init__(self, id, user_id, doctor_id, appointment_time, status, notes, created_at):
        self.id = id
        self.user_id = user_id 
        self.doctor_id = doctor_id 
        self.appointment_time = appointment_time # thời gian hẹn
        self.status = status
        self.notes = notes
        self.created_at = created_at

class Reminder:
    def __init__(self, id, appointment_id, reminder_time, reminder_type, sent_status):
        self.id = id
        self.appointment_id = appointment_id 
        self.reminder_time = reminder_time
        self.reminder_type = reminder_type
        self.sent_status = sent_status 

class AnonymousToken:
    def __init__(self, id, token, created_at, expires_at, is_active=True):
        self.id = id
        self.token = token 
        self.created_at = created_at
        self.expires_at = expires_at # ngày hết hạn của token
        self.is_active = is_active # trạng thái hoạt động của token

class Patient:
    def __init__(self, id, name, date_of_birth, gender, contact_info, created_at):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender=gender
        self.contact_info = contact_info # chứa object hoặc dict với thông tin liên hệ như email, phone
        self.created_at = created_at # ngày tạo bệnh nhân

class MedicalRecord:
    def __init__(self, id, patient_id, doctor_id, diagnosis,visit_date, treatment_plan, notes):
        self.id = id
        self.patient_id = patient_id 
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis # chứa thông tin chẩn đoán
        self.treatment_plan = treatment_plan # chứa kế hoạch điều trị
        self.notes = notes
        self.visit_date = visit_date # ngày khám bệnh

    class ARVProtocol:
        def __init__(self, id, code, name, description, for_group, created_at):
            self.id = id
            self.code = code
            self.name = name
            self.description = description # mô tả phác đồ
            self.for_group = for_group # nhóm bệnh nhân áp dụng phác đồ này
            self.created_at = created_at

class TreatmentHistory:
    def __init__(self, id, patient_id, arv_protocol, doctor_id, start_date, end_date, docrtor_id, notes):
        self.id = id
        self.patient_id = patient_id
        self.arv_protocol = arv_protocol # chứa thông tin về phác đồ ARV
        self.doctor_id = doctor_id
        self.start_date = start_date # ngày bắt đầu điều trị
        self.end_date = end_date # ngày kết thúc điều trị
        self.notes = notes  

    