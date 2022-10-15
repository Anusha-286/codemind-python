s=input()
s=s.lower()
v=['a','e','i','o','u']
l=[]
for i in s:
    if i in v:
        if i  not in l:
            l.append(i)
if len(v)==len(l):
    print(0)
else:
    for j in v:
        if j not in l:
            print(j,end=' ')