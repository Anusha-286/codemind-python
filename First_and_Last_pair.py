n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
l2=[]
for i in range(len(l)//2):
    l2.append(l[i])
    l2.append(l1[i])
if n%2!=0:
    x=len(l)//2
    l2.append(l[x])
    l2.append(0)
    print(*l2)
else:
    print(*l2)