
# ; Bài tập lâng cao:

# ; Thiết kế giao diện:
# ; ===================================================
# ; 1. Kiểm tra số dư
# ; 2. Rút tiền
# ; 3. Chuyển tiền
# ; 4. Sửa thông tin
# ;   - Khi bấm vào số (4) ra giao diện khác:
# ;       1. Sửa mật khẩu
# ;       2. Sửa số đt
# ;       3. Trở về 
# ; 5. Thoát
# ; ===================================================

# ; Người dùng sẽ bấm nút chọn (1), (2), ....

# ; '''
 
# ; # Gợi ý:

# ; def test():
# ;     giao_dien_chinh = """
# ;                 1. Kiểm tra số dư
# ;                 2. Rút tiền
# ;                 3. Chuyển tiền
# ;                 4. Sửa thông tin
# ;                 5. Thoát
# ;                 """#
# Mở nhiều tab quá hoặc chưa save cái j đó, nó chưa lưu lại. đúng ác
import json
account = json.load(open(r'F:\Hoc Python\Bank project\account.json'))
print('Chào mừng đến với Thụycombank ')

emails = []
for email in account:
    acc= account[email]
    if acc['balance'] >= 5000000:
        emails.append(email)

emails.sort()
for email in emails:
    print(email)



#=======================================================
def kiem_tra_so_du():
    email = input('Mời nhập id: ')
    if email in account:
        acc = account[email]
        pwd = input('Nhập pass vào : ')
        if pwd == acc['password']:
            print(f'Số dư của bạn là : {acc['balance']} ')
        else:
            print('Nhập sai mk rồi ')
    else:
        print('Không có dữ liệu id này')

#=======================================================
def rut_tien():
    email = input('Mời nhập id : ')
    if email in account:
        acc = account[email]
        pwd = input('Nhập pass vào : ')
        if pwd == acc['password']:
            rut = int(input('Nhập số tiền muốn rút : '))
            if rut <= acc['balance']:
                acc['balance'] -= rut
                print(f'đã rút thành công {rut}  từ tài khoản {email}.')
                with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
                    json.dump(account, f, indent= 3)
            else:
                    print('Rút tiền không thành công')
                
        else:
            print('Nhập sai pass rồi, mời nhập lại')

#=======================================================
def chuyen_tien():
    from_email = input('Mời nhập id muốn chuyển tiền : ')
    to_email = input('Mời nhập id nhận tiền : ')
    if from_email in account and to_email in account:
        from_acc = account[from_email]
        to_acc = account[to_email]
        pwd = input('Mời nhập pass: ')
        if pwd == from_acc['password']:
            chuyen_tien = int(input('Nhập số tiền muốn chuyển : '))
            if chuyen_tien <= from_acc['balance']:
                from_acc['balance'] -= chuyen_tien
                to_acc['balance'] += chuyen_tien
                with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
                    json.dump(account, f, indent= 2)
                print(f'đã chuyển thành công {chuyen_tien} từ {from_email} đến {to_email}')
            else:
                print('Tài khoản không đủ số dư')
        else:
            print('Nhập sai mật khẩu')
    else:
        print('Tài khoản không tồn tại')

#======================================================
def sua_thong_tin():
    '''
    ủa cái này sửa xong phải quay lại màn hình chính chứ,
    mặc định chỉnh xong quay về mh chính mới đúng
    '''
    email = input('Nhập id : ')
    if email in account:
        acc = account[email]
        pwd = input('Nhập pass vào : ')
        if pwd == acc['password']: 
            trove = False
            while trove == False: # ủa  chỗ này while true chi vậy , để nó back lại 1 vòng lặp , chứ về menu chính thì dễ r. nữa, cái số 4 nó khó lắm, k phải vậy đâu
                print('Chọn thông tin cần sửa : ')
                print('1.Password ')
                print('2.Số Phone ')
                print('3.Giới tính ')
                print('4.Quay về ')
                choice = int(input('Mời nhập lựa chọn: '))
                if choice == 1:
                    acc['password'] = input('Nhập pass cần đổi: ')
                    with open(r'F:\Hoc Python\Bank project\account.json','w+', encoding='utf-8') as f:
                        json.dump(account, f, indent=2)
                    print(f'Password của tài khoản {email} đã được đổi thành {acc['password']}. ')
                    
                elif choice == 2:
                    acc['phone']= input('Nhấp số Phone cần đổi : ')
                    with open(r'F:\Hoc Python\Bank project\account.json','w+', encoding='utf-8') as f:
                        json.dump(account, f, indent=2)
                    print(f'Số phone của {email} đã được đổi thành {acc['phone']}')

                    # break # break ngay chỗ này nó sẽ quay lại vòng lặp ban đầu
                    
                elif choice == 3:
                    print('1. Male')
                    print('2. Female')
                    print('3. Quay lại')
                    luilai= False
                    while luilai == False:
                        choose = int(input('Nhập giới tính: '))
                        if choose == 1 :
                            acc['gender'] = 'Male'
                            with open(r'F:\Hoc Python\Bank project\account.json','w+', encoding='utf-8') as f:
                                json.dump(account, f, indent=2)
                                print(f' giới tính của {email} đã được đổi thành {acc['gender']}')
                                luilai= True
                        elif choose == 2 :
                            acc['gender'] = 'Female'
                            with open(r'F:\Hoc Python\Bank project\account.json','w+', encoding='utf-8') as f:
                                json.dump(account, f, indent=2)
                                print(f' giới tính của {email} đã được đổi thành {acc['gender']}')
                                luilai = True
                        elif choose == 3 :
                            luilai = True #Hoặc Break để phá vòng lặp
                        else:
                            print('Nhập sai rồi bố.')
                            print('1. Male')
                            print('2. Female')
                            print('3. Quay lại')
                            luilai = False
                elif choice == 4:
                    trove = True
                else:
                    print('Nhập không đúng , mời nhập lại')
                    trove= False


        else:
            print('Nhập sai lựa chọn')  
    else: 
        print('Nhập sai id')

#===================================================
def kiemtra():
    
    giao_dien_chinh = """
        1. Kiểm tra số dư
        2. Rút tiền
        3. Chuyển tiền
        4. Sửa thông tin
        5. Thoát
"""
    exit= False
    while exit == False:
        print(giao_dien_chinh)
        choice = int(input('Mời bạn nhập : '))
        if choice == 1:
            kiem_tra_so_du() # ai chỉ đưa các hàm vô đây ?

        elif choice == 2:
            rut_tien() # ai chỉ đưa các hàm vô đây ?

        elif choice == 3:
            chuyen_tien() # ai chỉ đưa các hàm vô đây ?

        elif choice == 4:
            sua_thong_tin() # ai chỉ đưa các hàm vô đây ????? vậy cho nhanh, khúc này chắc chắn chatgpt hazz

        elif choice == 5:
            exit = True
            print('Thoát.')
        else: 
            print("Nhập sai mời nhập lại : ")
            exit= False

''''
ok tạm được, mai chuẩn bị nâng cao hơn nữa????? còn cái nào khó hơn ko?
'''

if __name__ == "__main__":
    # kiemtra()    

    students = []
    marks = []
    for s in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        marks.append(score)
    
    print(students)

    # students = [['thuy', 10.0], ['dat', 5.0], ['duy', 5.0], ['trieu', 8.0]]
    # s=3

    # marks.sort() # [5,5,8,10] [thuy, 8, 10 ,5]

    unique_marks = set(marks) # {8,10,5}, không sắp xếp
    unique_marks = list(unique_marks) # [8,10,5], có thể sắp xếp

    # unique_marks.sort() # hành động sắp xếp nhỏ -> lớn
    unique_marks = sorted(unique_marks)
    second_lowest = unique_marks[1]
    # print(second_lowest)

    names = []
    for student in students:
        name = student[0]
        mark = student[1]
        if mark == second_lowest:
            names.append(name)
            
    names.sort()
    for name in names:
        print(name)
   

                

            

