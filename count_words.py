s=input()
w=s.split()
c=0
v='aeiouAEIOU'
for i in w:
    if (i[0] in v) and (i[-1] not in v):
        c+=1
print(c)