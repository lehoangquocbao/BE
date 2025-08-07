# 🔌 Sơ đồ Flask API (HIV Treatment System)

```mermaid
flowchart TD
    subgraph AUTH [Xác thực]
        A1[POST /api/auth/register] --> A2[POST /api/auth/login]
    end

    subgraph NGUOI_DUNG [Người dùng]
        U1[GET /api/users] --> U2[GET /api/users/:id]
        U2 --> U3[PUT /api/users/:id]
        U3 --> U4[DELETE /api/users/:id]
    end

    subgraph BAC_SI [Bác sĩ]
        D1[GET /api/doctors]
        D2[POST /api/doctors]
        D3[PUT /api/doctors/:id]
        D4[DELETE /api/doctors/:id]
    end

    subgraph LICH_HEN [Lịch hẹn]
        AP1[GET /api/appointments]
        AP2[POST /api/appointments]
        AP3[PUT /api/appointments/:id]
        AP4[DELETE /api/appointments/:id]
    end

    subgraph XET_NGHIEM [Xét nghiệm]
        T1[GET /api/test-results]
        T2[POST /api/test-results]
        T3[PUT /api/test-results/:id]
    end

    subgraph DIEU_TRI [Điều trị]
        TR1[GET /api/treatments]
        TR2[POST /api/treatments]
        TR3[PUT /api/treatments/:id]
    end

    subgraph TU_VAN [Tư vấn]
        C1[GET /api/consultations]
        C2[POST /api/consultations]
        C3[PUT /api/consultations/:id]
    end

    subgraph THONG_BAO [Thông báo]
        N1[GET /api/notifications]
        N2[POST /api/notifications]
        N3[PUT /api/notifications/:id]
    end

    A2 --> U1
    U1 --> AP1
    U1 --> T1
    U1 --> TR1
    U1 --> C1
    U1 --> N1
