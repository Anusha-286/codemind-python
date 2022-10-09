n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
c=0
for i in l:
    if i not in l1:
        if i%k==0:
            l1.append(i)
print(len(l1))