day_so = input("Nhap vao mot day so bat ky, moi so cach nhau boi dau cach: ")
#Nhap vao day so "1 3 4 5 6 7 9 10 11 27 13 14 99 16 17 18 21 20"
if day_so[0] != "1":
    print("Day so phai bat dau tu so 1")
else:
    day_so_nguoc = day_so[::-1]
    pos = 0
    count = 0
    day_so_moi = ""
    for i in day_so_nguoc:
        if i == " ":
            k = day_so_nguoc[pos - count : pos]
            k = k[::-1]
            if int(k) % 2 != 0:
                day_so_moi = day_so_moi + k + " "
            count = 0
        else:
            count = count + 1
        pos = pos + 1
    day_so_moi = day_so_moi + "1"
    print(day_so_moi)