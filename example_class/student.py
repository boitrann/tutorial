
import json


students= json.load(open(r'F:\Repositories\tutorial\example_class\students.json'))


def update_students():
    with open(r'F:\Repositories\tutorial\example_class\students.json', 'w+', encoding='utf-8') as f:
        json.dump(students, f,indent=4 )



class Student:

    def __init__(self, truyenvao) -> None:  #Ham COnstructor
        self.id = truyenvao  
        '''
        ví dụ muốn tìm thông tin của 1 student thì không cần phải điền ID số lần muốn tìm
        nếu không có Class hoặc hàm constructor
        '''

    def get_phone(self):            # hàm bt
        phone = students[self.id]['phone']
        return phone
    
    def get_cccd(self):
        cccd = students[self.id]['cccd']
        return cccd
    
    def get_all_info(self):
        info = students[self.id]
        return info

    def modify_info(self, key_info, value_info):
        '''
        yeu cau: thay doi bat ky thong tin nao

        '''
        if  key_info in students[self.id]:
            students[self.id][key_info]= value_info
            update_students()
        else:
            print("thong tin nay khong co san")
            
    
        
        
    
    def edit_phone(self, new_phone):
        students[self.id]['phone'] = new_phone
        update_students()
        
    def add_student(hocsinh_id, name, class_name, phone, cccd):
        if hocsinh_id not in students:
            new_student = {
                "name": name,
                "class": class_name,
                "cccd": cccd,
                "phone": phone
                 }
            students[hocsinh_id] = new_student
            update_students()
        else: 
            print("ID da trung")
            
        
if __name__ == "__main__":
    student = Student(truyenvao= "01")
    phone = student.get_phone()
    print(phone)
    # cccd = student.get_cccd()
    # info = student.get_all_info()
    # # student.edit_phone("0901666666")
    # student.add_student(
    #     student_id= "03",
    #     name = "Duy",
    #     class_name = "9/10",
    #     cccd= "132132151",
    #     phone= "09055555555"
    # )