n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
    s+=l[i]
k=s//n
if k in l:
    print("True")
else:
    print("False")