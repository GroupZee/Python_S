'''class A:
    def __init__(self):#This is a method
        print("###Without arguments")
def main():
    first_object=A()
    second_object=A()
    
main()
print()
class B:
    def __init__(self,a,b):
        print("###With Arguments")
        print(a,b)
def main1():
    third_object=B(79.6+3,0)
    fourth_object=B(9-34,'Done')
main1()

print()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display (self):
        print(f"Name: {self.name}\nAge: {self.age}")
def main2():
    name=input("Enter your name: ")
    age=int(input("And age: "))
    abs(age)
    print()
    p1=person(name,age)
    p1.display()
main2()
print()

#passing a different number of arguments for a specific function
#Method Overloading
def product(q,w,e=None):
    if e is None:
        print(q*w)
    else:
        print(q*w*e)
product(23,-8)
product(-12.5,54,0.29)'''

#Method Overriding for single level inheritence
class q:
    def m1(self):
        print("Belongs to Q")
    def m2(self):
        print("Also belongs to Q")
class p(q):
    def m3(self):
        print("Belongs to P")
        
obj=p()
obj.m1()
