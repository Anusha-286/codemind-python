n=int(input())
s=str(n)
l=list(s)
a=1
b=0
for i in l:
    x=int(i)
    r=pow(x,a)
    b+=r
    a+=1
if b==n:
    print(True)
else:
    print(False)