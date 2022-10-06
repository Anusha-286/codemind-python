n=int(input())
s=str(n)
l=len(s)
sq=n**2
last=sq%pow(10,l)
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")