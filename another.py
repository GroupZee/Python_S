#nested while
choice="yes"
while choice!="no":
 num=int(input"(Enter any number"))
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
display() 
