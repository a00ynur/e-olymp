x = input()
a = 0
massiv = []

for i in x:
    if i=='k':
        a+=1
    else:
        a=0

    massiv.append(a)
print(max(massiv))