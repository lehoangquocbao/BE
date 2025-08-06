class appointment:
    def __init__(self, id, user_id, doctor_name,appointment_time, status="pending"):
        self.id=id
        self.user_id=user_id
        self.doctor_name=doctor_name
        self.appointment_time=appointment_time
        self.status=status

appointment=[]