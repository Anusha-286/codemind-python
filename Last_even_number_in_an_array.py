n=int(input())
l=list(map(int,input().split()))
a=l[::-1]
for i in range(0,len(l)):
    if a[i]%2==0:
        print(a[i])
        break
    