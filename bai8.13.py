#A = tổng các số lẻ nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(0, n+1):
    if i%2!=0:
        tong = tong + i
print(f"A = {tong}")

#B = tổng các số chẵn nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(0, n+1):
    if i%2==0:
        tong = tong + i
print(f"B = {tong}")

#C = tích các số từ 1 đến n
n = int(input("Nhap vao so nguyen duong n: "))
tich = 1
for i in range(1, n+1):
    tich = tich*i
print(f"C = {tich}")

#D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tich = 1
for i in range(1, n+1):
    if i%3==0:
        tich = tich*i
print(f"D = {tich}")

#E = tổng các số nguyên tố nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(2, n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        tong = tong + i
print(f"E = {tong}")

#F = tổng chuỗi đan dấu
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0.0
flag = True
for i in range(1, n+1):
    if flag == True:
        tong = tong + 1.0/i
        flag = False
    else:
        tong = tong - 1.0/i
        flag = True
print(f"F = {tong}")