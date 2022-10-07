n=int(input())
for i in range(n):
    a=input()
    for i in a:
        if i.isdigit()==True:
            print("Yes")
            break
    else:
        print("No")