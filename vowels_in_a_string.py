s=input()
v=input()
for j in s:
    if j==v:
        print(True)
        print(s.index(j))
        break
else:
    print(False)