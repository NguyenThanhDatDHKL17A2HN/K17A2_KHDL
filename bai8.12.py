x = int(input("Nhap vao so nguyen duong x: "))
if x < 2:
    print(x, " khong phai so nguyen to")
else:
    for i in range(2,x):
        if x%i == 0:
            print(x, "khong phai so nguyen to")
            break
    else:
        print(x, " la so nguyen to")