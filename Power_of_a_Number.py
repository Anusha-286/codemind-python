import math
x,y,m=map(int,input().split())
p=math.pow(x,y)
print(int(p%m))