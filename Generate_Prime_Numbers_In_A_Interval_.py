m=int(input())
n=int(input())
for i in range(m,n+1):
    if i==0 or i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)    