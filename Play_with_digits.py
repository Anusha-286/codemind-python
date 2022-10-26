n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    x=str(i)
    for j in x:
        y=int(j)
        s+=y
print(s)