import student



if __name__ == "__main__":
    s = student.Student(truyenvao= "02")
    print(s.get_cccd)
    s.modify_info(key_info= 'cccd', value_info= '1142421')

    # student.Student.add_student( # module.class.method
    #     student_id= input("Nhap id: "),
    #     class_name= input("Nhap class: "),
    #     name= input("Nhap name: "),
    #     phone= input("Nhap phone: "),
    #     cccd= input("Nhap cccd: ")
    # )
    
    # phonesss = s.get_phone()
    # print(phonesss)

