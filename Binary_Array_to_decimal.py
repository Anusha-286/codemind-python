n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
s=0
k=0
for i in l1:
    s+=i*(2**k)
    k+=1
print(s)