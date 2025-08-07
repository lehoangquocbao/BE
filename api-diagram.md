graph TD
  subgraph Vai_trò
    Khách
    Người_dùng
    Nhân_viên
    Bác_sĩ
    Quản_lý
    Quản_trị_viên
  end

  subgraph API_Công_khai
    A1[GET /thong-tin/co-so-y-te] --> Khách
    A2[GET /thong-tin/tai-lieu-giao-duc] --> Khách
    A3[GET /thong-tin/blog-kinh-nghiem] --> Khách
  end

  subgraph API_Xác_thực
    B1[POST /dang-ky] --> Người_dùng
    B2[POST /dang-nhap] --> Người_dùng
  end

  subgraph API_Người_dùng
    C1[GET /lich-hen] --> Người_dùng
    C2[POST /dat-lich-hen] --> Người_dùng
    C3[GET /ket-qua-xet-nghiem] --> Người_dùng
    C4[GET /phac-do-dieu-tri] --> Người_dùng
    C5[GET /bang-dieu-khien] --> Người_dùng
  end

  subgraph API_Bác_sĩ
    D1[GET /benh-nhan] --> Bác_sĩ
    D2[GET /benh-nhan/:id/xet-nghiem] --> Bác_sĩ
    D3[POST /benh-nhan/:id/phac-do] --> Bác_sĩ
    D4[POST /lich-tu-van] --> Bác_sĩ
  end

  subgraph API_Quản_lý
    E1[GET /nhan-vien] --> Quản_lý
    E2[POST /them-nhan-vien] --> Quản_lý
    E3[GET /bao-cao/tong-quan] --> Quản_lý
  end

  subgraph API_Quản_trị_viên
    F1[GET /nguoi-dung] --> Quản_trị_viên
    F2[POST /cap-quyen/:id] --> Quản_trị_viên
    F3[GET /cau-hinh-he-thong] --> Quản_trị_viên
  end

  subgraph API_Chung
    G1[GET /bang-dieu-khien] --> Nhân_viên
    G1 --> Bác_sĩ
    G1 --> Quản_lý
    G1 --> Quản_trị_viên

    G2[GET /thuoc] --> Bác_sĩ
    G2 --> Nhân_viên

    G3[GET /lich-lam-viec] --> Bác_sĩ
    G3 --> Nhân_viên
  end
