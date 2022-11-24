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
             6. insert marks
             7. view all marks
             8. subject wise mark
             9. subject wise average mark
             10. individual mark
             10. exit   
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
        print("search the  student : ")
        admno = input("Ënter the admission number")
        sql = 'SELECT `id`, `name`, `rollnumber`, `admno`, `college` FROM `students` WHERE `admno`= '+admno
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)    
    elif choice==4:
        print("update the student  ")
        admno = input("Enter the admission number : ")
        name = input("Enter the name to be update : ")
        rollno = input("Enter the roll number to be updated : ")
        college = input("Enter the college to be updated : ")
        sql = "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollno+"',`college`='"+college+"' WHERE `admno`=" +admno 
        mycursor.execute(sql)
        mydb.commit()
        print("Updated successfully")
    elif choice==5:
        print("delete the student  ")
        admino = input("Enter the admission number to be deleted : ")
        sql = 'DELETE FROM `students` WHERE admno = ' +admino
        mycursor.execute(sql)
        mydb.commit()
        print(f"{admino} Deleted successfully. ")
    elif choice==6:
        print("insert marks selected ")
        admno = input("Enter the student id : ")
        sql = 'SELECT `id` FROM `students` WHERE `admno`= '+admno
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print("student id is",id)
        
        physics = input("Enter the physics mark :")
        chemistry = input("Enter the chemistry mark : ")
        maths = input("Enter the maths mark : ")
        sql = "INSERT INTO `marks`(`student_id`, `physics_mark`, `chemistry_mark`, `maths_mark`) VALUES (%s,%s,%s,%s)"
        data = (id,physics,chemistry,maths)
        mycursor.execute(sql,data)
        result=mycursor.fetchall()
        mydb.commit()
        print("Marks inserted Successfully ")
    elif choice==7:
        print("view all mark")
        sql = "SELECT s.`name`, s.`rollnumber`, s.`admno`, s.`college`,m.physics_mark,m.chemistry_mark,m.maths_mark FROM `students` s JOIN  marks m ON s.id = m.student_id   "
        mycursor.execute(sql)
        result =mycursor.fetchall()
        for i in result:
            print(i)
    elif choice==8:
        print("subjectwise mark")
        subname= input("Enter the subject : ")
        if(subname=='physics'):
            sql = "SELECT `physics_mark` FROM `marks` "
        if(subname=='chemistry'):
            sql = "SELECT  `chemistry_mark` FROM `marks`"
        if(subname=='maths'):
            sql = "SELECT `maths_mark` FROM `marks` "
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice ==9):
        print("Subjectwise average marks")
        subname = input("Enter the subject name: ")
        if (subname=='physics'):
            sql="SELECT AVG (`physics_mark`) FROM `marks` "

        elif(subname =='chemistry'):
            sql="SELECT AVG (`chemistry_mark`) FROM `marks` "

        elif(subname =='maths'):
            sql="SELECT AVG (`maths_mark`) FROM `marks` "
        
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice == 10):
        print("Individual marks")
        adm = input("Enter the student admission number: ")
        sql = 'SELECT `id` FROM `students` WHERE `admno` =  '+adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        sql = "SELECT s.`name`, s.`rollnumber`, s.`admno`, s.`college`,m.physics_mark,m.chemistry_mark,m.maths_mark FROM `students` s JOIN marks m ON s.id = m.student_id WHERE s.id = "+id
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)





    



    elif choice==11:
        break
        