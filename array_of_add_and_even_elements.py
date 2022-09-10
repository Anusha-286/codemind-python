n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(0,len(l)):
    if l[i]%2!=0:
        a.append(l[i])
    else:
        b.append(l[i])
c=a+b
print(*c)