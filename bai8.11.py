n = int(input("Nhap so nguyen n: "))
x = float(input("Nhap so thuc x: "))
a = (x**2 + x + 1)**n + (x**2 - x + 1)**n
print(f"A = ({x}^2 + {x} + 1)^{n} + ({x}^2- {x} + 1)^{n} = {a}")