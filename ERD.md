# 🗂️ Sơ đồ ERD - Hệ thống quản lý điều trị HIV

```mermaid
classDiagram
    class NguoiDung {
        +String id
        +String hoTen
        +String email
        +String matKhau
        +String vaiTro
        +Date ngaySinh
    }

    class LichHen {
        +String id
        +Date ngayHen
        +String diaDiem
        +String trangThai
    }

    class BacSi {
        +String id
        +String chuyenKhoa
        +String maSoHanhNghe
    }

    class XetNghiem {
        +String id
        +String loai
        +Float giaTri
        +Date ngayTraKetQua
    }

    class DieuTri {
        +String id
        +String phacDo
        +Date ngayBatDau
        +String ghiChu
    }

    class LichLamViec {
        +String id
        +Date ngayLam
        +String caTruc
    }

    class TuVan {
        +String id
        +DateTime thoiGian
        +String chuDe
        +String trangThai
    }

    class ThongBao {
        +String id
        +String noiDung
        +Date ngayGui
        +Boolean daDoc
    }

    NguoiDung --> LichHen
    NguoiDung --> TuVan
    NguoiDung --> XetNghiem
    NguoiDung --> DieuTri
    NguoiDung --> ThongBao
    BacSi --> LichLamViec
    BacSi --> TuVan
