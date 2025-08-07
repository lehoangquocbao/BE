## 📌 API List - HIV Treatment and Medical Services System

```mermaid
graph TD

    subgraph "🔑 Auth & Roles"
        Guest["🔹 Guest"]
        Customer["👤 Customer"]
        Staff["👥 Staff"]
        Doctor["👨‍⚕️ Doctor"]
        Manager["🧑‍💼 Manager"]
        Admin["🛠️ Admin"]
    end

    subgraph "📚 Information & Education"
        InfoPage["📄 GET /info"]
        Blog["📝 GET /blog"]
    end

    subgraph "🩺 Medical Services"
        RegisterExam["📝 POST /register-exam"]
        BookAppointment["📆 POST /appointments"]
        ARVDelivery["📦 POST /arv-distribution"]
        Schedule["📋 GET /schedule"]
        LabResults["🧪 GET /lab-results"]
        TreatmentHistory["📑 GET /treatment-history"]
    end

    subgraph "🧠 AI Custom ARV Regimen"
        CustomARV["⚙️ POST /custom-arv"]
    end

    subgraph "📊 Dashboard & Reports"
        Dashboard["📊 GET /dashboard"]
        Reports["📈 GET /reports"]
    end

    subgraph "👨‍⚕️ Staff Management"
        Doctors["👨‍⚕️ GET /doctors"]
        Staffs["👥 GET /staff"]
        Schedules["📆 GET /doctor-schedule"]
    end

    Guest --> InfoPage
    Guest --> Blog
    Customer --> RegisterExam
    Customer --> BookAppointment
    Customer --> LabResults
    Customer --> TreatmentHistory
    Customer --> CustomARV
    Doctor --> Schedule
    Doctor --> ARVDelivery
    Doctor --> LabResults
    Doctor --> TreatmentHistory
    Manager --> Dashboard
    Manager --> Reports
    Admin --> Doctors
    Admin --> Staffs
    Admin --> Schedules
