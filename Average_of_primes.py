n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in l:
    if i==1:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s+=i
            c+=1
x=s/c
print("%.2f"%x)