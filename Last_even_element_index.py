n=int(input())
l=list(map(int,input().split()))
a=[]

for i in range(0,len(l)):
    if l[i]%2==0:
        a.append(i)
print(a[-1])