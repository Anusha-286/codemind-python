n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    s=str(abs(i))
    s1=len(s)
    if k==s1:
        c+=1
print(c)