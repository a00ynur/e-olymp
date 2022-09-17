number = int(input())
a = number // 100
b = (number // 10) % 10
c = number % 10
k = (a+b+c)**0.5
print(k)