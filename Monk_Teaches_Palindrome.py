n=int(input())
for i in range(n):
    a=input()
    l1=a[::-1]
    if a==l1:
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    