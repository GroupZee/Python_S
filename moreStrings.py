a="owierypwo"#you can use "string" or 'string' or '''For a paragraph'''
print(a)
b="owierypwo"
print(b[5])
print(b[-4])#one character
#for multiple characters, perform slicing
d="poiuytyuiop1"
print(d[-1::-1])#start,stop,step
print(d[0::1])
#using for loop
for u in d:
    print(u,end=' ')
    
#pal or not
print("\n")
word=input("Enter a word: ")
word1=word[::-1]
if word==word1:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")
#Capitalize first charater    
print(word.capitalize(),"has had its 1st character capitalized")
#get the index of a charater in a string
#print(word.index('j'))
#print(word.find('j'))
#print(word.isalpha())
#print(word.isalnum())
#print(word.isdecimal())
print(word.islower())#try number
print(word.isupper())
print(word.istitle())