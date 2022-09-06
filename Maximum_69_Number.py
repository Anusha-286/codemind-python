n=int(input())
c=str(n)
l=list(c)
l1=[]
cnt=0
for i in l:
    if i=='9':
        l1.append(i)
    elif i=='6':
        cnt+=1
        if cnt==1:
            l1.append("9")
            continue
        l1.append(i)
for j in l1:
    print(j,end='')