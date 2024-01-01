x = int(input("Nhap vao so nguyen duong x: "))
if x < 0:
    print("x phai la so nguyen duong")
else:
    if x == 0:
        print("0 khong phai la so hoan hao")
    tong = 0
    for i in range(1, x):
        if x%i==0:
            tong = tong + i
    if tong == x:
        print(x, "la so hoan hao")
    else:
        print(x, "khong phai so hoan hao")