# Tạo và mở tập tin để ghi văn bản
with open('HumptyDumpty.txt', 'w') as file:
# Ghi nội dung vào tập tin
    file.write("Humpty dumpty saton a wall,\n")
    file.write("humpty dumpty had a great fall.\n")
    file.write("All the king's horses and all the king's men\n")
    file.write("couldn't put Humpty together again.\n")           
print("Tập tin đã được tạo và ghi thành công.")
# Mở tập tin để đọc
try:
    with open('HumptyDumpty.txt', 'r') as file:
        # Đọc toàn bộ nội dung của tập tin
        content = file.read()
        
        # In nội dung của tập tin
        print(content)
except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
