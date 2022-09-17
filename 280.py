n=[int(i) for i in input().split()]
m = max(n)
n = min(n)
while m != 0 and n != 0:
    if m > n:
        m %= n
    else:
        n %= m
print(n + m)