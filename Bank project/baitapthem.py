import json
taikhoan = json.load(open(r'F:\Hoc Python\Bank project\account.json'))
# def themtaikhoan():
#     email = input('Nhập email vào: ')
#     if email in taikhoan.keys():
#         print('Email đã tồn tại')
#     else:
#         # password = input("nhập mk vào: ")
#         # phone = input('Nhập số đt vào : ')
#         # cccd = input("Nhập số cccd nè: ")
#         # gender = input("nhập giới tính vào : ")
#         # balance = int(input("nhập số dư vào : "))
#         taikhoan[email] = {
#             "password": input("nhập mk vào: "),
#             "phone": input('Nhập số đt vào : '),
#             "cccd ": input("Nhập số cccd nè: "),
#             "gender": input("nhập giới tính vào : "),
#             "balance": int(input("nhập số dư vào : "))
#     }
#     with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
#         json.dump(taikhoan,f, indent = 2)
# themtaikhoan()
def suathongtin():
    id = input('Nhập thông tin email: ')
    if id in taikhoan.keys():
        acc = taikhoan[id]
        pwd = input('Nhập mk : ')
        if acc['password'] == pwd:
            acc['password'] = input('Nhập mk muốn đổi : ')
            with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding = 'utf-8') as f:
                json.dump(taikhoan, f , indent =2)
            print(f'mật khẩu của {id} đổi thành {acc['password']}')
        else: 
            print('Sai mật khẩu')
    else: 
        return
# suathongtin()

# def xoa_tai_khoan():
#     id = input('Nhập id : ')
#     if id in taikhoan.keys():
#         acc = taikhoan[id]
#         pwd = input('Nhập mk: ')
#         if acc['password'] == pwd :
#             print('Bạn muốn xóa tài khoản không ?')
#             print('1.có ' )
#             print('2.không. ')
#             choice = int(input('Nhập lựa chọn:  '))
#             if choice == 1 :
#                 del taikhoan[id]
#                 with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
#                     json.dump(taikhoan, f, indent= 2)
#                 print(f' tài khoản {id} đã được xóa')
#             elif choice == 2 :
#                 return
#             else:
#                 print('Nhập sai rồi')
#         else:
#             print('Nhập sai mk rồi')
#     else :
#         return
# xoa_tai_khoan()

def them_acc():
    email = input('Nhập email : ')
    if email in taikhoan:
        print('Email đã tồn tại')
    else:
        taikhoan[email]= {
        "password": input('Nhập pw: '),
        "phone": input('Nhập phone: '),
        "cccd ": input('Nhập cccd: '),
        "gender": input('Nhập gender: '),
        "balance": int(input('Nhập số dư: '))
        }
        with open(r'F:\Hoc Python\Bank project\account.json','w+', encoding='utf-8') as f:
            json.dump(taikhoan,f , indent= 2)
        print(f'đã thêm {email} vào ')
# them_acc()

def sua_thong_tin():
    # Ví dụ muốn nhập thông tin cần sửa thì sao ? là sao?
    # Sao có mỗi sửa số đt vậy ?, vây test cho nhanh
    email = input('Nhập email: ')
    if email in taikhoan:
        taikhoan[email]['phone']= input('Sửa số dt thành : ')
        with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
            json.dump(taikhoan,f ,indent=2)
        print(f' số dt đổi thành {taikhoan[email]['phone']} ')
    else:
        return # else return là gì ? tới đó k chạy nữa. Chắc chắn chatgpt haizz
    


# sua_thong_tin()


'''
Bài tập lâng cao:

Thiết kế giao diện:
===================================================
1. Kiểm tra số dư
2. Rút tiền
3. Chuyển tiền
4. Sửa thông tin
  - Khi bấm vào số (4) ra giao diện khác:
      1. Sửa mật khẩu
      2. Sửa số đt
      3. Trở về 
5. Thoát
===================================================

Người dùng sẽ bấm nút chọn (1), (2), ....

'''
 
# Gợi ý:

def test():

    giao_dien_chinh = """
                1. Kiểm tra số dư
                2. Rút tiền
                3. Chuyển tiền
                4. Sửa thông tin
                5. Thoát
                """

    # rồi ok. Làm bài tập này đi. Gợi ý hết rồi đó 

    exit = False

    while exit == False: # Vòng lặp sẽ luôn chạy khi exit = False

        print(giao_dien_chinh)
        
        choice = int(input('Nhập lựa chọn: '))

        if choice == 5:
            '''
            Khi nào bằng 5 thì cho biến exit = True,
            khi nó quay trở lại vòng lặp nó kiểm tra exit mà khác False thì break
            '''
            exit = True
            print('Thoát.')
        
        elif choice == 1:
            pass 

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            # Thiết kế thêm giao diện
            pass



if __name__ == "__main__":
    test()