n=int(input())
l=list(map(int,input().split()))
ec=0
oc=0
for i in range(0,len(l)):
    if i%2==0:
        ec+=l[i]
    else:
        oc+=l[i]
diff=abs(oc-ec)
if diff==0:
    print("YES")
else:
    print("NO")