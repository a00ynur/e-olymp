num = int(input())
a = num % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10
e = num // 10000
print(10000*a + 1000*b + 100*c + 10*d +e)