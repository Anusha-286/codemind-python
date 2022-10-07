n=input()
a=0
for i in range(len(n)):
    if n.count(n[i])==1:
        d=i
        a+=1
        break
if a==0:
    print(-1)
else:
    print(d)