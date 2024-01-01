try:
    # Mở tập tin để đọc
    with open('HumptyDumpty.txt', 'r') as file:
        # Đọc nội dung của tập tin
        content = file.read()

        # Đếm số ký tự
        so_ky_tu = len(content)

        # Đếm số dòng
        so_dong = content.count('\n') + 1  # Đếm số dòng bằng cách đếm số ký tự xuống dòng và cộng thêm 1

        # Thống kê và in thông tin
        print(f"Tập tin có {so_ky_tu} ký tự.")
        print(f"Tập tin có {so_dong} dòng.")

except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")