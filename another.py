#nested while
choice="yes"
while choice!="no":
 num=int(input("Enter any number"))
 i=1
 while i<3:
  print(num,"x",i,"=",num*i)
  i+=1
 choice=input("Enter your choice")

#break
for x in range(1,68,3):
 print(x,end=' ')#end= defines how the print output should look like
 if x==27:
  break

#continue 
for x in range(1,68,3):
 print(x,' ')
 if x==27:
  continue 

#Functions
def display():
 for x in range(1,68):
  print(x,end=' ')
def subtract():
 n1=int(input("Number 1:"))
 n2=int(input("Number 2: "))
 if n1>n2:
  return n1-n2
 else:
  return n2-n1
def pint():
 print(subtract())
display() 
pint()
#more functions
def add(n1,m):
 print("The sum of",n1,"and",m,"is",n1+m)
def multi(d,a):
 return d*a
h=973
j=7384
add(h,j)
add(6738,92830)
