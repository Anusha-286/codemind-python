a=input()
v=0
c=0
d=0
s=0
l1=['a','e','i','o','u']
l2=['A','E','I','O','U']
for i in a:
    if i in l1:
        v+=1
    if i in l2:
        v+=1
    if i not in l1 and i not in l2:
        if i.isdigit()==True:
            d+=1
        elif i==' ':
            s+=1
        else:
            c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)