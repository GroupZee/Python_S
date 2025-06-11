try:
    f=open("Student1.txt","w")
    while True:
        rollno=input("Enter Roll Number:")#should check if it exists
        name=input("Name: ")
        course=input("Course: ")#should check if course exists
        print(rollno,name,course,file=f)
        ch=input("Add another?")
        if ch=="No" or ch=="no" or ch=="NO" or ch=="nO":
            break
except OSError:
    print("unable to creat file")
finally:
    f.close()