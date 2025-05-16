#Program to count vowels
name=str(input("Enter the word"))
v=0
for ch in name:
    if ch in "aeiouAEIOU":
        v+=1
print("The number of vowels is",v)        
