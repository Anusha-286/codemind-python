n=int(input())
s=str(n)
l=list(s)
c=0
d=0
for i in l:
    if int(i)%2==0:
        c+=1
    elif int(i)%2!=0:
        d+=1
if len(l)==c:
    print("Even")
elif len(l)==d:
    print("Odd")
else:
    print("Mixed")