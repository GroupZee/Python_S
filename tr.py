n=int(input("Enter a number"))
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
##Multiplication
m=int(input("Enter a number"))
i=0
while i<11:
    p=m*i
    print(m,"*",i,"=",p)
    i+=1
#Factorial
e=int(input("Enter a number"))
facto=1
while e>0:
    facto=facto*e
    e=e-1
print("Factorial is",facto)

