# 📘 Sơ đồ ERD (HIV Treatment System)

```mermaid
classDiagram
    class User {
        +String id
        +String name
        +String email
        +String password
        +String role
        +Date dob
    }

    class Appointment {
        +String id
        +Date appointmentDate
        +String location
        +String status
    }

    class Doctor {
        +String id
        +String specialization
        +String licenseNumber
    }

    class TestResult {
        +String id
        +String type
        +Float value
        +Date resultDate
    }

    class Treatment {
        +String id
        +String regimen
        +Date startDate
        +String note
    }

    class Schedule {
        +String id
        +Date workDate
        +String shift
    }

    class Consultation {
        +String id
        +DateTime time
        +String topic
        +String status
    }

    class Notification {
        +String id
        +String message
        +Date sendDate
        +Boolean read
    }

    User --> Appointment
    User --> Consultation
    User --> TestResult
    User --> Treatment
    User --> Notification
    Doctor --> Schedule
    Doctor --> Consultation
