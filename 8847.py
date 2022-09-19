n = int(input())
right = n // 1000
left = n % 1000
a = left // 100
b = left // 10 % 10
c = left % 10
print(right * 1000 + c * 100 + b * 10 + a)