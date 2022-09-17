n = int(input())
sum = 0

sum = sum + n // 500
n = n % 500

sum = sum + n // 200
n = n % 200

sum = sum + n // 100
n = n % 100

sum = sum + n // 50
n = n % 50

sum = sum + n // 20
n = n % 20

sum = sum + n // 10
n = n % 10

if n < 10 and n > 0:
    print(-1)
    exit()

if sum == 10:
    print(-1)
else:
    print(sum)