from secrets import choice


while True:
    print("select an option from the menu")
    print("""             1. add student
             2. view all students
             3. search a student
             4. update the student
             5. delete a student
             6. exit   
                 """)
    choice =int(input("Enter your option : "))
    if choice==1:
        print("student entry selected")
    elif choice==2:
        print("view all student selected ")
    elif choice==3:
        print("search the  student  ")
    elif choice==4:
        print("update the student  ")
    elif choice==5:
        print("delete the student  ")
    elif choice==6:
        break