num = int(input())
a = num % 10
b = num // 100 % 10
c = num // 10000
print(c*100 + b*10 + a)