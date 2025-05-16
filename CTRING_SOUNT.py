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
for value in range(0,81):
    print(value,end=" ")

#print alphabet in lower case and upper case
for v in range(65,92):
    print(chr(v),end=' ')
    
for v in range(97,123):
    print(chr(v),end="\n")