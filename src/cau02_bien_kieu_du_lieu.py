# 5 & 6. Tạo các biến theo quy tắc snake_case với kiểu dữ liệu phù hợp: str, int, float, bool, NoneType
ma_phien = "LAB026"
ma_may = "PC12"
cong_suat_w = 250.0
thoi_gian_phut = 90
dang_hoat_dong = True
ghi_chu = None

# 7. In từng giá trị và dùng type() để kiểm tra kiểu
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất (W):", cong_suat_w, "| Kiểu:", type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))
print("Đang hoạt động:", dang_hoat_dong, "| Kiểu:", type(dang_hoat_dong))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))

# 8. Thay thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian_phut = 120
print("Thời gian sử dụng mới (phút):", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))