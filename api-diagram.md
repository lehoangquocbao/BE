graph TD
  subgraph VaiTro
    guest[Khách]
    user[Nguoi_dung]
    staff[Nhan_vien]
    doctor[Bac_si]
    manager[Quan_ly]
    admin[Quan_tri_vien]
  end

  subgraph API_CongKhai
    A1[GET /thong-tin/co-so-y-te] --> guest
    A2[GET /thong-tin/tai-lieu-giao-duc] --> guest
    A3[GET /thong-tin/blog-kinh-nghiem] --> guest
  end

  subgraph API_XacThuc
    B1[POST /dang-ky] --> user
    B2[POST /dang-nhap] --> user
  end

  subgraph API_NguoiDung
    C1[GET /lich-hen] --> user
    C2[POST /dat-lich-hen] --> user
    C3[GET /ket-qua-xet-nghiem] --> user
    C4[GET /phac-do-dieu-tri] --> user
    C5[GET /bang-dieu-khien] --> user
  end

  subgraph API_BacSi
    D1[GET /benh-nhan] --> doctor
    D2[GET /benh-nhan/:id/xet-nghiem] --> doctor
    D3[POST /benh-nhan/:id/phac-do] --> doctor
    D4[POST /lich-tu-van] --> doctor
  end

  subgraph API_QuanLy
    E1[GET /nhan-vien] --> manager
    E2[POST /them-nhan-vien] --> manager
    E3[GET /bao-cao/tong-quan] --> manager
  end

  subgraph API_QuanTriVien
    F1[GET /nguoi-dung] --> admin
    F2[POST /cap-quyen/:id] --> admin
    F3[GET /cau-hinh-he-thong] --> admin
  end

  subgraph API_Chung
    G1[GET /bang-dieu-khien] --> staff
    G1 --> doctor
    G1 --> manager
    G1 --> admin

    G2[GET /thuoc] --> doctor
    G2 --> staff

    G3[GET /lich-lam-viec] --> doctor
    G3 --> staff
  end
