t=int(input())
for _ in range(t):
    n=int(input())
    nv=n
    while True:
        nc=0
        for i in range(1,nv+1):
            if nv%i==0:
                nc+=1
        if nc==2:
            break
        nv+=1
    pv=n
    while True:
        pc=0
        for j in range(1,pv+1):
            if pv%j==0:
                pc+=1
        if pc==2:
            break
        pv-=1
    if n-pv<=nv-n:
        print(pv)
    else:
        print(nv)
