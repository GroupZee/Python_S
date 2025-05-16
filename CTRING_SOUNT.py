#Program to count vowels
name=str(input("Enter the word"))
v=0
for ch in name:
    if ch in "aeiouAEIOU":
        v+=1
print("The number of vowels is",v)        
#ord plus a character give ASCII value e.g C=67 ord("C") 
#chr plus ASCII give character 93=]
#range(start,stop,step)
for value in range(0,8):
    print(value,end=" ")
print("\n")
#print alphabet in lower case and upper case
for v in range(65,91,3):
    print(chr(v),end=' ')
print("\n")
for v in range(97,123):
    print(chr(v),end=" ")
    
print("\n")   
#Nested loop
for f in range(1,11):
    for g in range(10,21):
        print(g,end=' ')#prints row
    print(f,end="\n")#prints column