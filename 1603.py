n = int(input())
if n < 0:
    n *= -1
sum = 0
while n>0:
    k = n % 10
    n = n // 10
    sum = sum + k
print(sum)