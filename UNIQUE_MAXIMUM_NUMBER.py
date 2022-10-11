n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[]
for i in s:
    if l.count(i)==1:
        l1.append(i)
if len(l1)==0:
    print(-1)
else:
    print(max(l1))