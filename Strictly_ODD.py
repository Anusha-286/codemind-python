n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,len(l)):
    if i%2!=0 and l[i]%2!=0:
        continue
    elif l[i]%2!=0:
        a.append(i)
if len(a)==0:
    print(True)
else:
    print(False)