class User:
    def __init__(self, id, username, email, password, created_at, is_anonymous=False):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_anonymous = is_anonymous

class Doctor:
    def __init__(self, id, name, specialty, email, phone, created_at):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.email = email
        self.phone = phone
        self.created_at = created_at

class Appointment:
    def __init__(self, id, user_id, doctor_id, appointment_time, status, notes, created_at):
        self.id = id
        self.user_id = user_id
        self.doctor_id = doctor_id
        self.appointment_time = appointment_time
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
        self.expires_at = expires_at
        self.is_active = is_active
