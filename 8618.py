n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n  % 10
if 1000*a + 100*b + 10*c + d == 1000*d + 100*c + 10*b + a:
    print("YES")
else:
    print("NO")