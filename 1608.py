s = input() 

polindrom = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        polindrom = False
        break

if polindrom:
    print("Yes")
else:
    print("No")