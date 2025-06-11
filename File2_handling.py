def sth():
 try:
    f=open("Student1.txt","w")
    while True:
        rollno=input("Enter Roll Number:")#should check if it exists
        name=input("Name: ")
        course=input("Course: ")#should check if course exists
        print(rollno,name,course,file=f)
        ch=input("Add another?")
        if ch=='yes' or ch=='Yes' or ch=='YES':
            continue
        elif ch=="No" or ch=="no" or ch=="NO" or ch=="nO":#accepts only yes
            break
        else:
            print("I don't understand your answer")
            break
 except OSError:
    print("unable to creat file")
 finally:
    f.close()
def addd():
    try:
        f=open("Student1.txt","a")
        while True:
            rollno=input("Enter Roll Number:")#should check if it exists
            name=input("Name: ")
            course=input("Course: ")#should check if course exists
            print(rollno,name,course,file=f)
            ch=input("Add another?")
            if ch=='yes' or ch=='Yes' or ch=='YES':
                print("Okay!")
                continue
            elif ch=="No" or ch=="no" or ch=="NO" or ch=="nO":#accepts only yes
                break
            else:
                print("I don't understand your answer")
                break
    except OSError:
        print("unable to creat file")
    finally:
        f.close()
#addd()

file_p='Student1.txt'
from collections import Counter
def many(file_p):
    with open(file_p) as file:
        words=file.read().lower().split()
        for word, count in Counter(words).most_common(5):
            print(word,count)

#many(file_p)           
# from File_handling import display2
# File_handling.display2()