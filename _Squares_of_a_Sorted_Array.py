n=int(input())
l=list(map(int,input().split()))
l1=[]
a=0
for i in l:
    a=int(i)*int(i)
    l1.append(a)
l1.sort()
print(*l1)