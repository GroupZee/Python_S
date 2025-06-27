import mysql.connector
'''
def main():
    cn=mysql.connector.connect(database="d1",user="root",password="admin@123")
    c=cn.cursor()
    while True:
        rollno=int(input("Enter rollno:"))
        name=input("Enter a name:")
        sub1=int(input("Marks for subject1:"))
        sub2=int(input("Marks for subject2:"))
        sub3=int(input("Marks for subject3:"))
        cmd="insert into stud_marks values(%s,%s,%s,%s,%s)"
        c.execute(cmd,params=(rollno,name,sub1,sub2,sub3))
        k=c.rowcount
        if k==1:
            print("Student added successfully")
            cn.commit()
        ans=input("Add another one?")
        if ans=="no":
            break
main()
'''
'''
def main1():
    cn=mysql.connector.connect(database="d1",user="root",password="admin@123")
    c=cn.cursor()
    c.execute("select * from stud_marks")
    #stud1=c.fetchone() or fetchall()
    #print(stud1)
    a=c.fetchmany(2)
    print(a)
main1()
'''
'''
def mine():
    cn=mysql.connector.connect(database="d1",user="root",password="admin@123")
    c=cn.cursor()
    while True:
        rollno=int(input("Enter rollno to delete:"))
        c.execute("DELETE FROM stud_marks WHERE rollno= %s",(rollno,))#similar to mysql commands
        if c.rowcount>0:
            print("Delete successfully")
            cn.commit()
        else:
            print("Not found")
        an=input("Delete another?")
        if an.lower()=='no':
            break
    cn.close()
mine()
'''
def mine1():
    cn=mysql.connector.connect(database="d1",user="root",password="admin@123")
    c=cn.cursor()
    c.execute("update stud_marks set name='Jk' where rollno=90323")
    cn.commit()
mine1()
