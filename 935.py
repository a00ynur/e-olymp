n = int(input())
if n < 0:
    n *= -1
a = n // 100
b = n // 10 % 10
c = n % 10 
print(a,b,c, sep="\n")