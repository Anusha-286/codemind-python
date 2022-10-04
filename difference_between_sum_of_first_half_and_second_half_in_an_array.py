n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(0,len(l)):
    if i<n//2:
        a+=l[i]
    else:
        b+=l[i]
print(abs(a-b))