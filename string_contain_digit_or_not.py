n=input()
c=0
for i in n:
    if i.isdigit()==True:
        c+=1
if c>0:
    print("Contains",c,"digit")
else:
    print("Doesn't contain digit")