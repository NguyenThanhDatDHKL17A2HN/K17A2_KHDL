def nhap_canh():
    while True:
        try:
            a = float(input("Nhập cạnh a: "))
            b = float(input("Nhập cạnh b: "))
            c = float(input("Nhập cạnh c: "))
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError("Các cạnh của tam giác phải là số dương.")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Tổng hai cạnh bất kỳ phải lớn hơn cạnh còn lại.")
            return a, b, c
        except ValueError as e:
            print("Lỗi: ", str(e))

a, b, c = nhap_canh()
print(f"Tam giác với các cạnh {a}, {b}, {c} hợp lệ.")
