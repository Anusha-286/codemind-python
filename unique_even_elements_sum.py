n = int(input())
l=list(map(int,input().split()))
l1=[]
s=0
for i in l:
    if i not in l1:
        l1.append(i)
        if i%2==0:
            s+=i
print(s)