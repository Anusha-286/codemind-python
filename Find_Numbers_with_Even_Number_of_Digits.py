n=int(input())
l=list(map(int,input().split()))
ec=0
for i in l:
    s=str(i)
    if len(s)%2==0:
        ec+=1
print(ec)