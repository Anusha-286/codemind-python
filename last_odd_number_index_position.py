n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(0,len(l)):
    if i%2!=0:
        a.append(i)
    c+=1
print(c-1)