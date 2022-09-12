t,s,b=map(int,input().split())
capacity=2*s*t*b*512
total=capacity//1024
s=str(total)
print(s+"KB")