n=int(input())
s=str(n)
l=list(s)
if int(l[0])!=0 and len(l)==10:
    print("Valid")
else:
    print("Invalid")