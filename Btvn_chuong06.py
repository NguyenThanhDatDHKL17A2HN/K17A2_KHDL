#1.1
print("**    **  ******    **      **     ******")
print("**    **  **        **      **     **  **")
print("********  ******    **      **     **  **")
print("**    **  **        **      **     **  **")
print("**    **  ******    ******  ****** ******")
#1.2
x = 10
y = 5
tong = x+y
hieu = x-y
tich = x*y
thuong = x/y
print('x = 10, y = 5')
print('Tổng x+y', '=',tong)
print('Hiệu x-y', '=', hieu)
print('Tích x*y', '=', tich)
print('Thương x/y', '=', thuong)
#1.3
ten_hang = "Sữa hộp Vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Đơn giá: 250000")
print("Tiền phải trả:", "{:,} vnd".format (tien_phai_tra))
#1.4
yeu_cau_1 = (5 - 3) // 2
print("(5-3)//2", "=", yeu_cau_1)
yeu_cau_2 = (8-3*2)-(1+1)
print("(8-3*2)-(1+1)", "=", yeu_cau_2)
#1.5
So_luong= int(input("Nhập số lượng:"))
Don_gia= int(input("Nhâp đơn giá:"))
print("Thành tiền=", So_luong, "*", Don_gia, "=", So_luong*Don_gia)