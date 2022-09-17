number = int(input())

a = number // 1000
b = (number // 100) % 10
c = (number // 10) % 10
d = number % 10
x = (a+b) + (c+d)

print(x**2)