n = int(input()) #123
x = (n // 10 % 10) * 100 + (n // 100) * 10 + n % 10
print(x)