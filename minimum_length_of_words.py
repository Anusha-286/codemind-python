s=input()
a=s.split()
l=[]
for i in a:
    l.append(len(i))
print(min(l))