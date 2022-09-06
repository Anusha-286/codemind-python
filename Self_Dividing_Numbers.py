m=int(input())
n=int(input())
a=[]
for i in range(m,n+1):
    if i<=9:
        a.append(i)
    elif i>=9 and i%10!=0:
        c=str(i)
        cnt=0
        for j in c:
            if i%int(j)==0:
                cnt+=1
        if len(c)==cnt:
            a.append(i)
print(*a)