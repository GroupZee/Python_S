marks=float(input("enter marks:"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
else:
    print("C")
## strings
mark=str(input("enter marks:"))
if mark=="End":
    if marks==50:
        print("END")
    else:
        print("We are not sure")
else:
    print("Still not sure")
###Login
print("\n\n\nLOGIN")
user=input("Username:")
passw=input("Password:")
if user=='pusr29':
    if passw=='pusr29':
        print("\nWelcome")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")