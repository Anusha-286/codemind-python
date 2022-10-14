s=input()
res=s.split()
l1=[]
for i in res:
    l1.append(len(i))
print(max(l1))