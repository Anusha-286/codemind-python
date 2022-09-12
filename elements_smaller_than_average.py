n=int(input())
l=list(map(int,input().split()))
s=sum(l)
avg=s//n
c=0
for i in range(0,len(l)):
    if l[i]<=avg:
        c+=1
print(c)