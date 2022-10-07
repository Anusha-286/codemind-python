m=int(input())
n=int(input())
s=m+n
for i in range(s+1,s**2):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            x=i
            break
print(x-s)