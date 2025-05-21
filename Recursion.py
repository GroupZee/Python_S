def calc(n,m,opr):
    def add():
        return n+m
    def sub():
        return n-m
    def mult():
        return n*m
    def div():
        return n/m
    if opr=='+':
        print(add())
    if opr=='-':
        print(sub())
    if opr=='*':
        print(mult())
    if opr=='/':
        print(div())
##recursion_factorial
def fact(j):
    if j==0:
        return 1
    else:
        return j*fact(j-1)
    
k=int(input("Enter a number"))
print(fact(k))




x=int(input("Enter n:"))
y=int(input("Enter m:"))
z=str(input("Enter operator:"))
calc(x,y,z)