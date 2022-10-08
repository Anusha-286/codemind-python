n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=l1+l2
l=[]
for i in l3:
    if (i in l1) and (i in l2):
        if i not in l:
            l.append(i)
print(*l)