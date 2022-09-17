number = 2
a = input()
b = ""
for n in range(1, 1001):
    number = 2 ** n
    b += str(number)
    if(a == b):
        print(n)
        break