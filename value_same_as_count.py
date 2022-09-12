n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i==l.count(i):
        l1.append(i)
s=set(l1)
print(len(s))