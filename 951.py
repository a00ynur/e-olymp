number = int(input())
a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
result = a * 1000 + c * 100 + b * 10 + d

print(result)