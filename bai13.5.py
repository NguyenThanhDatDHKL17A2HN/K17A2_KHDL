import csv

def write_csv_file(file_name, content):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            # Tạo đối tượng ghi CSV
            writer = csv.writer(file)

            # Ghi nội dung vào tập tin CSV
            for row in content:
                writer.writerow(row)
            
            print(f"Đã ghi nội dung vào tập tin '{file_name}'.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin CSV cần tạo và ghi nội dung(cuối file .csv): ")

    content = []
    while True:
        row = input("Nhập nội dung cho dòng (nhập '0' để kết thúc): ")
        if row.lower() == '0':
            break
        content.append(row.split(','))

    write_csv_file(file_name, content)

if __name__ == "__main__":
    main()
