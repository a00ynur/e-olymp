n = int(input())
right = n // 100
left = n % 100
a = left // 10
b = left % 10
print(right * 100 + b * 10 + a)