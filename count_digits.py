n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=str(abs(i))
    s1=len(s)
    l1.append(s1)
print(*l1)