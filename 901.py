a=input()
s=0
for i in range(1,len(a)):
    if a[i]=='+' or a[i]=='-' or a[i]=='*':
        s+=1
print(s)