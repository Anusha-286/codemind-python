n=int(input())
l=[]
for i in range(1,n+1):
    if i==1:
        continue
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
if n in l:
    s=str(n)
    c=0
    for i in s:
        if int(i) in l:
            c+=1
    if len(s)==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
        
                