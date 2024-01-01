def chuong11_bai1():
    a=[1,2,3]
    b=[1,[2,3]]
    c=[]
    d=[1,2,3][1:]
    #Độ dài của các danh sách trên
    print('Độ dài list a:',len(a))
    print('Độ dài list b:',len(b))
    print('Độ dài list c:',len(c))
    print('Độ dài list d:',len(d))

def chuong11_bai2(): 
    # Danh sách các đội, thứ tự giảm dần từ đọi tốt nhất
    teams=[['Steven','Neena','Lex','Alexander','Bruce'],['David','Jack','Bill','Tom','Mike','Daniel'],
    ['Alexander','Adam','Payam','Kevin','Sigal','Mike']]
    # Đứng đầu danh sách là huấn luyện viên tiếp theo là đội trưởng 
    print(teams[-1].pop(1))

def chuong11_bai3():
    animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
    print('List of animals:',animals)
    print('Number of animals:',len(animals))
    a=input('I want to find: ')
    l = a in animals
    if l ==True:
        print('There is',a,'in list of animals')
    else:
        print('There is not',a,'in list of animals')

def chuong11_bai4():
    mylist=[]
    while True:
     val=int(input("Nhập giá trị : "))
     a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
     mylist.append(val)
     if a==0:
         x=int(input("Nhập giá trị cần tìm x:"))
         break
    print('List:',mylist) 
    print('Tổng các giá trị trong list:',sum(mylist))
    print(x,'xuất hiện',mylist.count(x),'trong list')
    if max(mylist)==x:
        print(x,'lớn hơn tất cả các số trong list')
    else:
       print(x,'không lớn hơn tất cả các số trong list')
    newlist=[int(i) for i in mylist if int(i)>x]
    print('Các số lớn hơn',x,'trong list',newlist)

def chuong11_bai5():
    mylist=[]
    while True:
        val=int(input("Nhập giá trị : "))
        a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
        mylist.append(val)
        if a==0:
          break
    print('List:',mylist)
    am=[int(i) for i in mylist if int(i)<0]
    print('Các phần tử âm trong list:',am)
    print('Trung bình cộng các phần tử âm',sum(am)/len(am))
    duong=[int(i) for i in mylist if int(i)>0]
    print('Các phần tử dương trong list:',duong)
    print('Trung bình cộng các phần tử dương',sum(duong)/len(duong))
    print('Giá trị max trong list',max(mylist))
    print('Giá trị min trong list',min(mylist))
    mylist.sort()
    print('List sắp tăng dần:',mylist)

def chuong11_bai6():
    chieu_cao=[74,74,72,72,73,69,69,71,76,71]
    def doi(x):
        return x*0.0254
    ccmoi = [doi(x) for x in chieu_cao]
    print('Đổi inch sang m:',ccmoi)
    print('In 3 chiều cao đầu tiên:',ccmoi[0:3])
    print('In 3 chiều cao cuối cùng:',ccmoi[-3:])
    print("Chiều cao max:",max(ccmoi))
    print("Chiều cao min:",min(ccmoi))
    print("Chiều cao trung bình:",sum(ccmoi)/len(ccmoi))
    ccmoi.sort()
    print('Chiều cao tăng dần:',ccmoi)
    ccmoi.sort()
    ccmoi.reverse()
    print('Chiều cao giảm dần:',ccmoi)

def chuong11_bai7():
    L=[1,2,3,4,5]
    thresh=2
    def elementwise_greater_than(L,thresh):
        for x in range(0,5):
            if L[x] > thresh:
                  L[x]=True
            else:
                L[x]=False    
        return L
    print(elementwise_greater_than(L,thresh))

def chuong11_bai8():
    nums= [2,6,7,9]
    def has_lucky_number(nums):
     for x in nums:
         if nums[x]%7==0:
            return True
         else:
            return False
    print(has_lucky_number(nums))

def chuong11_bai9():
    arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
    def party_late(arrivals,name):
        if name==arrivals[-1]:
            return False
        elif name==arrivals[0]:
            return False
        elif name==arrivals[1]:
            return False
        elif name==arrivals[2]:
            return False
        elif name==arrivals[3]:
            return False
        else:
            return True
    print(party_late(arrivals,name='Gilber'))
    print(party_late(arrivals,name='Ford'))
    print(party_late(arrivals,name='Mona'))

def chuong11_bai10():
    def menu_is_boring(meals):
        for i in range(len(meals)-1):
            if meals[i] == meals[i+1]:
                return True
        return False
    meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
    meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
    print(menu_is_boring(meals_1))
    print(menu_is_boring(meals_2))

def chuong11_bai14():
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
