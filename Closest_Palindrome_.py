n=int(input())
l1=[]
l2=[]
for i in range(100,2*n):
    x=str(i)
    y=x[::-1]
    if x==y:
        if int(y)<n:
            l1.append(i)
        elif int(y)>n:
            l2.append(i)
a=max(l1)
b=min(l2)
if (n-a)<(b-n):
    print(a)
elif (n-a)>(b-n):
    print(b)
else:
    print(a,b)