import json

customers = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\customer\customers.json', encoding= 'utf-8'))
print(customers) # load được mà ?


def update_customer():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\customer\customers.json','w+', encoding='utf-8') as f:
        json.dump(customers,f , indent= 3)

class Customers:
    def __init__(self, taikhoan) -> None:
        self.email = taikhoan

    def get_info(self):
        thongtin_all = customers[self.email]
        return thongtin_all
    
    def get_id(self):
        id = customers[self.email]["id"]
        return id
    
    def get_name(self):
        name = customers[self.email]["name"]
        return name
    
    def get_phone(self):
        phone = customers[self.email]["phone"]
        return phone
    
    def edit_customer(self, key_edit, value_edit):
        if key_edit in customers[self.email]:
            customers[self.email][key_edit] = value_edit
            update_customer()
        else:
            print('Thông tin cần sửa sai')       
              
if __name__ == "__main__":
    customer = Customers(taikhoan = "customer1@gmail.com")
   
    # phone = customer.get_phone()
    # print(phone)
    customer.edit_customer(key_edit="name",value_edit="Nguyễn Văn A")
    