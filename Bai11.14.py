#Tạo một danh bạ 
danh_ba={'Minh':'0989741258','Hạnh':'0903852147','Bình':'0913753951','An':'0933753654','Linh':'0813138951'}
while True:
    a=int(input("Bạn muốn làm gì ? 1: Tìm thông tin trong danh bạ; 2: Thêm liên hệ mới "))
    if a==1:
    #Tìm thông tin trong danh bạ theo tên
        a=input("Nhập tên cần tìm: ")
        if a in danh_ba:
            print('Thông tin của',a,'trong danh bạ là:\n',a,":",danh_ba[a])   
        else:
            print("Người này không nằm trong danh bạ")
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break
    elif a==2:
    #Thêm 1 liên hệ mới
        b=input("Tên liên hệ mới :")
        c=input("Số điện thoại liên hệ mới:")
        danh_ba[b]=c
        print('Danh bạ điện thoại :')
        for i in danh_ba:
            print(i,':',danh_ba[i])
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break

