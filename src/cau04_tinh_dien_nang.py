# Trường hợp 1: so_phut = 90
# Dự đoán: dien_nang_kwh = 0.375 (float), chi_phi = 1125.0 (float)
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13 & 14. Tính điện năng tiêu thụ, chi phí điện và in giá trị kèm kiểu dữ liệu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- Khi số phút = 90 ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

# 16. Thay so_phut bằng 60 rồi tính lại và so sánh
# Dự đoán: dien_nang_kwh = 0.25 (float), chi_phi = 750.0 (float)
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- Khi thay số phút = 60 ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))