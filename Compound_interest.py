p,r,t=map(int,input().split())
a=p*(1+(r/100))**t
a=("%.2f"%a)
print(a)