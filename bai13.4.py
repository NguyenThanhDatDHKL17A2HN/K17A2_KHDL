def write_to_file(file_name, content):
    try:
        # Mở tập tin trong chế độ ghi
        with open(file_name, 'w') as file:
            # Ghi nội dung vào tập tin
            file.write(content)
        print(f'Đã ghi nội dung vào tập tin {file_name}')

        # Đọc và in nội dung tập tin sau khi ghi
        read_and_print_file(file_name)

    except Exception as e:
        print(f'Lỗi: {e}')

def read_and_print_file(file_name):
    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc và in nội dung tập tin
            file_content = file.read()
            print(f'Nội dung của tập tin {file_name} sau khi ghi:')
            print(file_content)
    except FileNotFoundError:
        print(f'Tập tin {file_name} không tồn tại.')

def main():
    # Nhập tên tập tin từ người dùng
    file_name = input('Nhập tên tập tin (.txt): ')

    # Kiểm tra xem tên tập tin có kết thúc bằng .txt hay không
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    # Nhập nội dung từ người dùng
    content = input('Nhập nội dung: ')

    try:
        # Mở tập tin trong chế độ đọc
        with open(file_name, 'r') as file:
            # Đọc nội dung cũ của tập tin
            old_content = file.read()

            # Kiểm tra nếu có nội dung cũ
            if old_content:
                # Xóa nội dung cũ
                write_to_file(file_name, content)
            else:
                # Ghi nội dung mới vào tập tin
                write_to_file(file_name, content)

    except FileNotFoundError:
        # Tập tin chưa tồn tại, tạo tập tin và ghi nội dung vào
        write_to_file(file_name, content)

if __name__ == "__main__":
    main()
def main():
    while True:
        choice = int(input("Người dùng có muốn tiếp tục ghi nữa hay không? (1 để tiếp tục, 0 để dừng): "))
        
        if choice == 1:
            # Ghi tiếp tục
            print("Đang tiếp tục ghi...")
            # Thêm mã của bạn ở đây
            
        elif choice == 0:
            print("Người dùng đã chọn dừng. Kết thúc chương trình.")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
