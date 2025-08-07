graph TD
    NguoiDung["📦 NguoiDung API"]
    ThongBao["📦 ThongBao API"]
    DieuTri["📦 DieuTri API"]
    XetNghiem["📦 XetNghiem API"]
    TuVan["📦 TuVan API"]
    LichHen["📦 LichHen API"]
    BacSi["📦 BacSi API"]
    LichLamViec["📦 LichLamViec API"]

    NguoiDung -->|has| ThongBao
    NguoiDung -->|has| DieuTri
    NguoiDung -->|has| XetNghiem
    NguoiDung -->|has| TuVan
    NguoiDung -->|has| LichHen
    BacSi -->|has| LichHen
    BacSi -->|has| LichLamViec
