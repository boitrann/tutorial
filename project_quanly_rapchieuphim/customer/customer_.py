import json

customers = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\customer\customers.json', encoding= 'utf-8'))
print(customers) # load được mà ?


def update_customer():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\customer\customers.json','w+', encoding='utf-8') as f:
        json.dump(customers,f , indent= 2)


class Customers:
    def __init__(self, taikhoan) -> None:
        self.email = taikhoan

    def get_info(self):
        thongtin_all = customers[self.email]
        return thongtin_all
    
    def get_id(self):
        id = customers[self.email]["id"]
        return id
    
    def get_name(self,phimnao):
        name = customers[self.email][phimnao]["name"]
        return name
    
    def get_phone(self,phimnao):
        phone = customers[self.email][phimnao]["phone"]
        return phone
    
    def edit_customer(self, key_edit, value_edit):
        if key_edit == customers[self.email]:
            customers[self.email][key_edit]= value_edit
            update_customer()
        else:
            print('Thông tin cần sửa sai')       
              
if __name__ == "__main__":
    customer = Customers(taikhoan = "customer1@gmail.com")
   
    customer.edit_customer(key_edit="phone",value_edit="0901555666")
    # Customers.edit_customer(key_edit= "phone", value_edit= "0901222255")