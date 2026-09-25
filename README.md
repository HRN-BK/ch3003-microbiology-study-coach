# Gram+ · CH3003 Vi sinh vật học

Trang web ôn thi cuối kì môn Vi sinh vật học (CH3003): lịch "Học hôm nay" tự xếp, 45 bài học chi tiết kèm phần mở rộng thực tế, 485 câu trắc nghiệm, 3 đề thi thử 50 câu / 70 phút, 16 bài giải mẫu, 459 từ vựng và 207 thẻ ghi nhớ.

## Mở trang
Mở `index.html` bằng trình duyệt (chạy offline, tiến độ lưu trong trình duyệt).

## Sửa nội dung
- Nội dung nằm trong `content/*.py` (mỗi file một nhóm: `his`, `bac`, `fun`, `ctl`, `gro`, `pro`, `vir`, `idt`, `app`), dùng các hàm trong `content/_lib.py`.
- Giao diện và logic nằm trong `app.html`.
- Build lại sau khi sửa:

```bash
python3 build.py          # kiểm tra dữ liệu + tạo index.html
python3 build.py --json   # thêm data/db.json để xem dữ liệu
```

Chi tiết thiết kế: `PLAN.md`.
