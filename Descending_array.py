n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    j=i+1
    if j<n:
        if l[i]>l[j]:
            c+=1
if c+1==n:
    print("yes")
else:
    print("no")