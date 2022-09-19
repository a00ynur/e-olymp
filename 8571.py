n = input()
n = n.lower()
s = str(input())

c=0
for i in n:
    if i==s[0] :
        c+=1
print(c)
