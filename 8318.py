a = input()
b = []

for i in a:
    if i != "3" and i != "9":
        b.append(i)


print(*b, sep="")