ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# Lỗi 1 (Dòng 6 - SyntaxError: '(' was never closed): Thiếu dấu đóng ngoặc đơn ')' ở cuối hàm print().
# Lỗi 2 (Dòng 4 - TypeError: unsupported operand type(s) for /: 'str' and 'int'): Biến cong_suat_w chưa được ép kiểu sang float nên mang kiểu str, không thể thực hiện phép chia số học.
# Lỗi 3 (Dòng 6 - NameError: name 'dien_nang' is not defined): Gọi sai tên biến dien_nang thay vì tên biến đúng đã khai báo ở dòng 4 là dien_nang_kwh.