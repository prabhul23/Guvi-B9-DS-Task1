import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="learning")
cur = con.cursor()  

def add_student():
    Name = str (input("Enter Name of Student: "))
    School = str(input("Enter your School Name: "))
    Eng= int(input("Enter Marks for English: "))
    Maths = int(input("Enter Marks for Maths: "))
    Malay = int(input("Enter Marks for Malayalam: "))
    Science = int(input("Enter Marks for Science: "))
    Soc_Sci = int(input("Enter Marks for Social Science: "))
    Total_Marks = Eng+Maths+Malay+Science+Soc_Sci
    Avg = round(Total_Marks/5)
    Grade = calc_grade(Avg)

    cur.execute(
            """INSERT INTO STUDENT (Name, School,Eng,Maths,Malay,Science,Soc_Sci,Grade) VALUES (\"""" + Name + """\",\"""" + School+ """\",""" + str(
                Eng) + """,""" + str(Maths) + """,""" + str(Malay) + """,""" + str(Science) + """,""" + str(
                Soc_Sci)+ """,\"""" + Grade + """\")""")
    con.commit()            

def calc_grade(Avg):
    if (Avg >= 80):
        Grade = 'A'
    elif (Avg > 60 and Avg < 80):
        Grade = 'B'
    elif (Avg > 40 and Avg < 60):
        Grade = 'C'
    else:
        Grade = 'D'
    return Grade


def get_student():
    stud = str(input("Enter name of Student you want to find: "))
    cur.execute("""SELECT * from STUDENT where Name =\""""+stud+"""\";""")
    result = cur.fetchall()
    for i in result:
        print(i)


def get_all_student():
    cur.execute("SELECT * FROM STUDENT")
    result = cur.fetchall()
    for i in result:
        print(i)


def update_student():
    name = str(input("enter the name: "))
    cur.execute("""Select Name from STUDENT where Name =\"""" + name + """\";""")

    name1 = cur.fetchone()
    for i in name1:
        name2 = i

    def update_name():
        new_name = str(input("Enter new name of student: "))
        cur.execute("""UPDATE 
                           STUDENT
                       SET
                           Name = REPLACE(Name,\"""" + name + """\",\"""" + new_name + """\")
                       WHERE
                           Name IS NOT NULL;""")
        con.commit()
    


    def update_school():
        school_name = str(input("enter the old school name: "))
        new_schoolname = str(input("enter the new school name: "))
        cur.execute("""UPDATE 
                            STUDENT
                       SET
                            School = REPLACE(School,\"""" + school_name + """\",\"""" + new_schoolname + """\")
                       WHERE
                            School IS NOT NULL;""")
        con.commit()

    def update_mark(Subject):
        cur.execute("""SELECT """+Subject+""" FROM STUDENT where Name =\"""" + name + """\";""")
        Mark = cur.fetchone()
        for i in Mark:
            nMark = i
        cur.execute("""select """+Subject+""" from STUDENT where Name =\"""" + name + """\";""")
        totalMark = cur.fetchone()
        for i in totalMark:
            totalMark = i

        old_grade = calc_grade(totalMark/5)
        new_total = totalMark - nMark
        new_mark = int(input("enter the new subject mark: "))
        updated_total = new_mark + new_total
        new_Avg = round(updated_total/5)
        new_grade = calc_grade(new_Avg)
        cur.execute("""UPDATE
                            STUDENT
                       SET
                            """+Subject+""" = REPLACE("""+Subject+""",""" + str(nMark) + """,""" + str(new_mark) + """),                            
                            Grade = REPLACE(Grade,\"""" + old_grade + """\",\"""" + new_grade + """\")
                       WHERE
                            Name=\""""+name+"""\";""")
        con.commit()

    while (True):

        if name2 != name:
            print("Enter correct name of student!!")
            break
        elif name2 == name:
            print("1. Update Name:")
            print("2. Update Name of School:")
            print("3. Update English Marks:")
            print("4. Update Maths Marks:")
            print("5. Update Malayalam Marks:")
            print("6. Update Science Marks:")
            print("7. Update Social Science Marks:")
            print("8. Exit")
            x = int(input("Enter your choice: "))
            if x == 1:
                update_name()
            elif x == 2:
                update_school()
            elif x == 3:
                update_mark("Eng")
            elif x == 4:
                update_mark("Maths")
            elif x == 5:
                update_mark("Malay")
            elif x == 6:
                update_mark("Science")
            elif x == 7:
                update_mark("Soc_Sci")
            elif x == 8:
                break
        else:
            break


def delete_student():
    stud_name = str(input("Enter name of student whose details are to be deleted: "))
    cur.execute("""DELETE FROM STUDENT WHERE Name= \"""" + stud_name + """\";""")
    con.commit()
    print("Student details has been deleted!!")

while(True):
    print('Menu')
    print('1. Add Student Details')
    print('2. Get Student Details')
    print('3. Get all Student Details')
    print('4. Update Student Details')
    print('5. Delete Student Details')
    print('6. Exit')
    n = int(input("Select your choice: "))
    if n == 6:
        print(" ****Exit****")
        break
    elif n == 1:
        add_student()
    elif n == 2:
        get_student()
    elif n == 3:
        get_all_student()
    elif n == 4:
        update_student()
    elif n == 5:
        delete_student()
    else:
        print("Invalid choice")
        break








