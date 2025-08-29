from .class_appointment import (
    db,
    User,
    Doctor,
    Appointment,
    Reminder,
    AnonymousToken,
    Patient,
    MedicalRecord,
    ARVProtocol,
    TreatmentHistory,
    Role
)

# Để khi import models sẽ có sẵn các class
__all__ = [
    "db",
    "User",
    "Doctor",
    "Appointment",
    "Reminder",
    "AnonymousToken",
    "Patient",
    "MedicalRecord",
    "ARVProtocol",
    "TreatmentHistory",
    "Role"
]
