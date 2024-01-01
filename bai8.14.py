n = int(input("Nhap so cac so nguyen: "))
if n < 0:
    print("n khong hop le")
else:
    tong = 0
    for i in range(1,n+1):
        a = int(input(f"Nhap so nguyen thu {i}:", ))
        tong = tong + a
    print("Tong cac so vua nhap:", tong)