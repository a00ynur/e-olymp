n = int(input())
if n < 0:
    n = -1 * n
teklik = n % 10
while n > 9:
    n = n // 10
print(n+teklik)