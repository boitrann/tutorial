import json

employees = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\employee\employees.json'))
def update_employee():
    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\employee\employees.json', 'w+', encoding='utf-8') as f:
        json.dump(employees, f, indent = 2)
class Employees:
    def __init__(self,truyenvao) -> None:
        self.nhanvien = truyenvao
    def get_info(self):
        thongtin_all= employees[self.nhanvien]
        return thongtin_all
    def get_name(self):
        name = employees[self.nhanvien]['name']
        return name
    def edit_info(self,key_edit, value_edit):
        if key_edit in employees[self.nhanvien]:
            employees[self.nhanvien][key_edit]= value_edit
            update_employee()
        else:
            print('Khong co thong tin can sua')
if __name__=="__main__":
    nhanvien =Employees(truyenvao="employee1@gmail.com" )
    # thongtin_all = nhanvien.get_info()
    print(nhanvien.get_info())

    # name = nhanvien.get_name()
    # print(name)
    
    nhanvien.edit_info(key_edit="password", value_edit="1234567")
    

        
        