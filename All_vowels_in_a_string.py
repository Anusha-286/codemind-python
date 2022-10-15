s=input()
s=s.split()
m=''.join(s)
k=m.lower()
v=['a','e','i','o','u']
l=[]
for i in m:
    if i in v:
        if i not in l:
            l.append(i)
if len(l)==len(v):
    print(True)
else:
    print(False)