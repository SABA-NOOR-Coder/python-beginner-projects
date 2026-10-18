students = []
print("===== Student Record System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")
while True:
    choice = int(input("Enter your choice:"))

    if choice == 1:
        name = input("Enter Student Name:")
        age = int(input("Enter Student Age:"))
        roll_no = int(input("Enter Student Roll no:"))
        marks = int(input("Enter Student Marks:"))
        student = {"name":name, 
           "age":age,
           "roll_no":roll_no,
           "marks":marks}
        students.append(student)
        print(students)
        print("===== Student Added Successfully =====")
    elif choice ==2:
        if len(students) == 0:
            print("Student Record Not Found")
        for student in students:
            print(student["name"])
            print(student["age"])
            print(student["roll_no"])
            print(student["marks"])
    elif choice == 3:
        user_roll_no = int(input("Enter Roll no:"))
        for student in students:
            if student["roll_no"] == user_roll_no:
                print(student)
                break
        else:
            print("Student Record Not Found")
    elif choice == 4:
        user_roll_no = int(input("Enter Roll no:"))
        for student in students:
            if student["roll_no"] == user_roll_no:
                student["name"] = input("Enter Student Name:")
                student["age"] = input("Enter Student age:")
                student["roll_no"] = input("Enter Student Roll no:")
                student["marks"] = input("Enter Student Marks:")
                print("Student Update Successfully")
                break
        else:
            print("Student Record does not chnage")
    elif choice == 5:
        user_roll_no = int(input("Enter Roll no:"))
        for student in students:
            if student["roll_no"] == user_roll_no:
                students.pop()
                print("Student Deleted Successfully")
                break
        else:
            print("Student Record Not Found")
              
    elif choice == 6:
        print("Thank You💙")
        break

    
    else:
        print("======== Coming Soon ========")


    