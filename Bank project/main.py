import json 


account = json.load(open(r'F:\Hoc Python\Bank project\account.json')) # Load file account.json -> dictionary

# account = json.load(open(r'F:\Hoc Python\Bank project\account.json'))
# print(account.keys())

# def add_balance(email): # Nap tien
#     if email in account.keys():

#         # Nhap mat khau
#         pwd = input("Vui long nhap mat khau: ")

#         acc = account[email]
#         pw = acc['password']
#         if pw == pwd:
#             amount = int(input('so tien nap vao: '))
#             original_balance = acc['balance']
#             new_balance = original_balance + amount
#             acc['balance'] = new_balance

#             print(f'Added {amount} to account {email}') 

#             with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
#                 json.dump(account, f, indent=2) # update lai file account.json
#         else:
#             print('Nhap sai pw roi')

#     else:
#         print(f'Account `{email}` does not exist.')



# add_balance(email=input('Nhap email vao : '))


'''
    1. Kiểm tra số dư
    2. Nạp tiền
    3. Chuyển tiền
    4. Đổi thông tin số điện thoại
    5. Xóa tài khoản
'''

# ===============================================================

# email= input('Nhap email: ')

# if email in account.keys():
#     user = account[email]
#     pw = input('Nhap mat khau: ')
#     if pw == user['password']:
#         print('So Du la : ', user['balance'])
#     else:
#         print('Nhap sai pw, moi nhap lai')
# else:
#     print('Sai Tai khoan')


# print(account['vinhthuy102@gmail.com']['balance'])
#================================================================

# email = input('Nhap email: ')
# if email in account.keys():
#     user = account[email]
#     sodu = user['balance']
#     pw = user['password']
#     pwd = input('Nhap mat khau : ')
#     if pw == pwd :
#         print('So du la : ',sodu)
#     else:
#         print('Nhap sai mk roi pa ')
# else:
#     print('Nhap sai tai khoan')


#================================================================

# def add_balance ():
    
# id = input('Nhap id  : ')
# if id in account.keys():
#         acc = account[id]  # account(account.keys())
#         pawd = input('Nhap mat khau: ')
#         if pawd == acc['password']:
#             print('so du la : ',acc['balance'])
#             amount = int(input("Nhap so tien can nap: "))
#             original_balance = acc['balance']
#             new_balance = original_balance + amount
#             acc['balance'] = new_balance  # acc['balance'] phai ở bên trái mới đúng
#             with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
#                 json.dump(account, f, indent=2) # update lai file account.json
#                 print('so du moi la : ', new_balance)

#         else:
#             print('nhap sai roi')
# else:
#         print('sai id roi')
# add_balance () # nếu tự nhập số liệu thì hàm def () không cần parameter bên trong

def transfer_money():
    from_email = input('Nhập email chuyển tiền : ')
    to_email = input('Nhập email nhận tiền : ')
    if from_email in account.keys() and to_email in account.keys():
        from_acc= account[from_email]
        to_acc = account[to_email]
        from_pw = input('Nhập mk tai khoan chuyen: ')
        if from_pw == from_acc['password']:
            chuyentien= int(input('Nhap so tien chuyen: '))
            if chuyentien <= from_acc['balance']:
                 print(f'chuyen thanh cong {chuyentien} đến {to_email}')
                 from_original_balance = from_acc['balance']
                 from_new_balance = from_original_balance - chuyentien
                 from_acc['balance']= from_new_balance
                 to_original_balance = to_acc['balance']
                 to_new_balance = to_original_balance + chuyentien
                 to_acc['balance'] = to_new_balance
                 with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
                    json.dump(account, f, indent=2) # update lai file account.json

            else:
                print('tai khoan khong du so du')
# transfer_money()
            
# ===============================================================
# def tele_update():
#     email = input('Nhap email vao : ')
#     if email in account.keys():
#         acc = account[email]
#         print(acc)
#         tele = input('Nhap so dien thoai muon doi : ')
#         acc['phone']= tele
#         with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
#             json.dump(account, f, indent=2)
#         print(acc)
#     else:
#         print('Nhap sai roi')
# # tele_update()

#================================================================
def xoa_acc():
    id_can_xoa = input('Nhap email can xoa: ')
    if id_can_xoa in account.keys():
        acc = account[id_can_xoa]
        pw = input('Nhap pass vao : ')
        if pw == acc['password']:
            xoa_id = account.pop(id_can_xoa) #khúc này chắc chắn ChatGPT haizz, hoặc del cũng dc -del acc
            with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
                json.dump(account, f, indent=2)
            print(f'tai khoan {id_can_xoa} đã được xóa.')
        else:
            print('Nhập sai pw')
    else:
        print('Nhập sai tài khoàn')
# xoa_acc()


def chuyentien():
    from_id = input('Nhap vao id cần chuyển tiền: ')
    to_id = input('Nhập id muốn chuyển tiền vào : ')
    if from_id in account.keys() and to_id in account.keys():
        from_acc = account[from_id]
        to_acc = account[to_id]

        # nâng cao
        while True:
            pwd = input('Nhập mật khẩu:  ')

            if from_acc['password'] == pwd: 
                chuyentienne = int(input('Nhap so tien can chuyen : ')) # chỗ này, khi nào nhập đúng mới cho input tiên

                if from_acc['balance'] >= chuyentienne:
                    from_original_balance = from_acc['balance']
                    from_new_balance = from_original_balance - chuyentienne
                    from_acc['balance']= from_new_balance
                    to_original_balance = to_acc['balance']
                    to_new_balance = to_original_balance + chuyentienne
                    to_acc['balance'] = to_new_balance
                    with open(r'F:\Hoc Python\Bank project\account.json', 'w+', encoding='utf-8') as f:
                        json.dump(account, f, indent=2)
                else:
                    print('TK không đủ số dư')
                
                break # Khi nào nhập mk ok đúng thì chạy hết từ trên xuống dưới, sau đó thoát khỏi vòng lặp while True

            else: 
                print('Mật khẩu sai. Mời nhập lại, hoặc nhấn Ctrl + C để thoát')


# má nhập sai mk, nhập tiền chi ? 
# ok, mà nên chặn ngay lúc nhập sai mk

xoa_acc()



# đúng nưhaaa haizz , bt
        




    
    
    





