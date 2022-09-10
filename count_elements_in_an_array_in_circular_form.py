n=int(input())
l=list(map(int,input().split()))
l.append(l[0])
l.append(l[1])
c=0
for i in range(0,len(l)):
    j=i+2
    if j<len(l):
        if l[i]%2==0 and l[j]%2!=0:
            c+=1
        elif l[i]%2!=0 and l[j]%2==0:
            c+=1
print(c)
