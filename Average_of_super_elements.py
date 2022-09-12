n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[]
for i in s:
    if i==l.count(i):
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    k=sum(l1)/len(l1)
print("%.2f"%k)
