n=int(input())
l=list(map(int,input().split()))
c=0
s=set(l)
for i in s:
    if i%2!=0:
        c+=1
print(c)