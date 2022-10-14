n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(abs(i))
    l1.append(len(s))
l2=[]
for j in range(0,len(l1)):
    if max(l1)==l1[j]:
        l2.append(l[j])
print(*l2)