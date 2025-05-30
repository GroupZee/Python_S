'''a=[12,122,32435,'as',45.233,-54]
print(type(a))
#updating
a[0]=120
a[1:3:]=['asad','fderer']
a.append("lashd")#adding elements
print(a[0::1])
#a.clear()
#del a[3]
#a.pop()
#using append
n=int(input("Enter number of players: "))
scores=[]
for i in range(n):
    r=int(input("enter the scores: "))
    scores.append(r)
print("Total score is:",sum(scores))
print("Max is:",max(scores))
print("Min is:",min(scores))'''


#program to perform stack operation
stack=[]
while True:
    print("1.Push\n2.Pop\n3.View\n4.Exit")
    choice=int(input("Choose an option: "))
    match(choice):
        case 1:
            new=input("Enter a new element: ")
            stack.append(new)
            print(new,"has been pushed")
        case 2:
            if len(stack)==0:
                print("Stack is empty, can't pop.")
            else:
                stack.pop()
        case 3:
            print(stack)#could choose a specific element to print
        case 4:
            break
        case _:
            print("Invalid input")
                
        
    
    