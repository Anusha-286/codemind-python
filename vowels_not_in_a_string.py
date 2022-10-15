s=input()
n=s.lower()
v=['a','e','i','o','u']
l=[]
for i in n:
    if i in v:
        if i not in l:
            l.append(i)
if len(l)==len(v):
    print(0)
else:
    for j in v:
        if j not in l:
            print(j,end=' ')