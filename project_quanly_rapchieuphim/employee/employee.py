import json

employees = json.load(open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\employee\employees.json'))
def update_employee():

    with open(r'F:\Repositories\tutorial\project_quanly_rapchieuphim\employee\employees.json', 'w+', encoding='utf-8') as f:
        json.dump(employees, f, indent = 2)

class Employees:
    def __init__(self,employee_email) -> None:
        self.employee_ = employee_email

    def get_info(self):
        all_employee_info = employees[self.employee_]
        return all_employee_info
    
    def get_name(self):
        name = employees[self.employee_]['name']
        return name
    
    def edit_info(self,key_edit, value_edit):
        if key_edit in employees[self.employee_]:
            employees[self.employee_][key_edit]= value_edit
            update_employee()
        else:
            print('Khong co thong tin can sua')

if __name__=="__main__":
    employee_def =Employees(employee_email="employee1@gmail.com" )
    all_employee_info = employee_def.get_info()
    print(employee_def.get_info())

    name = employee_def.get_name()
    print(name)
    
    employee_def.edit_info(key_edit="password", value_edit="1234567")
    

        
        