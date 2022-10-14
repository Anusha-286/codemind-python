s=input()
x=s.lower()
c=0
for j in x:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        c+=1
print(c)