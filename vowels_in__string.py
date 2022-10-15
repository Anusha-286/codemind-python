s=input()
l=[]
l1=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in l1:
        if i not in l:
            l.append(i)
print(*l)