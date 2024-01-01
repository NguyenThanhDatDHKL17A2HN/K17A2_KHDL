n = int(input("Nhap so nguyen duong n: "))
x = int(input("Nhap so nguyen x: "))
if n < 0:
    print("n khong hop le")
else:
    tong = 0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua = giai_thua*i
        tong = tong + (x**i)/giai_thua
    print(f"e^{x} = {tong}")