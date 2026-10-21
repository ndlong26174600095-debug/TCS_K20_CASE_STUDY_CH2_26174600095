from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Bổ sung tính thời lượng
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

# 24. Dự đoán kết quả của phép trừ: 1:50:00, kiểu dữ liệu là datetime.timedelta
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# 25. Giải thích sự khác nhau giữa datetime, str và timedelta:
# - datetime (datetime.datetime): Biểu diễn một mốc thời gian cụ thể (năm, tháng, ngày, giờ, phút, giây...), có thể dùng để tính toán thời gian.
# - str: Chuỗi văn bản thuần túy biểu diễn thời gian đã định dạng để hiển thị cho người dùng đọc, không trực tiếp cộng/trừ thời gian được.
# - timedelta (datetime.timedelta): Biểu diễn khoảng thời gian chênh lệch (thời lượng) giữa hai mốc datetime.