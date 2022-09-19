n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
if (a==b==c!=d) or (a==c==d!=b) or (a==b==d!=c) or(b==c==d!=a):
    print("YES")
else:
    print("NO")