# 17. Dùng input() để nhận bốn giá trị và in type() của chúng ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
cong_suat_raw = input("Nhập công suất (W): ")
so_phut_raw = input("Nhập số phút sử dụng: ")
don_gia_raw = input("Nhập đơn giá điện/kWh: ")

print("Kiểu dữ liệu ngay sau khi nhập:")
print("ma_may:", type(ma_may))
print("cong_suat_raw:", type(cong_suat_raw))
print("so_phut_raw:", type(so_phut_raw))
print("don_gia_raw:", type(don_gia_raw))

# 18. Chuyển công suất sang float, số phút sang int và đơn giá sang float
cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

print("Kiểu dữ liệu sau khi chuyển kiểu:")
print("cong_suat_w:", type(cong_suat_w))
print("so_phut:", type(so_phut))
print("don_gia_kwh:", type(don_gia_kwh))

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Mã máy:", ma_may)
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí điện (VND):", chi_phi)