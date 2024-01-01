import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            # Đọc tập tin CSV
            reader = csv.reader(file)
            
            # In nội dung từng dòng
            for row in reader:
                print(row)
                
    except FileNotFoundError:
        print(f"Tập tin '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def write_phone_numbers(file_name, phone_numbers):
    try:
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
            # Tạo đối tượng ghi CSV
            writer = csv.writer(file)

            # Ghi danh sách số điện thoại và tên người vào cuối tập tin
            for phone_number, person_name in phone_numbers:
                writer.writerow([person_name, phone_number])

            print(f"Đã ghi danh sách số điện thoại vào cuối tập tin '{file_name}'.")
    
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin CSV cần ghi số điện thoại và tên vào: ")

    phone_numbers = []
    while True:
        person_name = input("Nhập tên người (nhập 'done' để kết thúc): ")
        if person_name.lower() == 'done':
            break
        phone_number = input("Nhập số điện thoại: ")
        phone_numbers.append((phone_number, person_name))

    write_phone_numbers(file_name, phone_numbers)

    # Xuất nội dung tập tin vừa ghi
    print("\nNội dung tập tin sau khi ghi:")
    read_csv_file(file_name)

if __name__ == "__main__":
    main()
