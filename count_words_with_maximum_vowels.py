s=input()
w=s.split()
v=['a','e','i','o','u']
l=[]
for i in w:
    c=0
    for j in i:
        if j in v:
            c+=1
    l.append(c)
e=l.count(max(l))
print(e)