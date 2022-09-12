n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
for i in l:
    if l.count(i)==k:
        if i not in l1:
            l1.append(i)
if len(l1)==0:
    print(-1)
else:
    print(*l1)