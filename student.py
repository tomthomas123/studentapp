from unittest import result
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root' ,password = '',database = 'studentdb')

mycursor = mydb.cursor()
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
        name = input("enter the name :")
        rollno =input("Enter the roll no :  ")
        adno = input("Enter the admission number : ")
        college =input("Enter the collegename : ")
        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollno,adno,college)
        mycursor.execute(sql,data)
        mydb.commit()
    elif choice==2:
        print("view all student selected ")
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif choice==3:
        print("search the  student  ")
    elif choice==4:
        print("update the student  ")
    elif choice==5:
        print("delete the student  ")
    elif choice==6:
        break
        