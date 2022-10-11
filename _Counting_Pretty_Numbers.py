t=int(input())
for i in range(t):
    l,m=map(int,input().split())
    c=0
    for j in range(l,m+1):
        r=l%10
        if r==2 or r==3 or r==9:
            c+=1
        l+=1
    print(c)
            