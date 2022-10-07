a=input()
l=list(a)
for i in range(len(l)):
    if l[i]==".":
        l[i]="[.]"
a="".join(l)
print(a)