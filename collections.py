a=[12,122,32435,'as',45.233,-54]
print(type(a))
a.append("lashd")#adding elements
print(a[0::1])
#using append
n=int(input("Enter number of players: "))
scores=[]
for i in range(n):
    r=int(input("enter the scores: "))
    scores.append(r)
print("Total score is:",sum(scores))
print("Max is:",max(scores))
print("Min is:",min(scores))