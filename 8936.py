n, m  = map(int, input().split())
for i in range(m, n-1, -1):
    if i % 2 == 0:
        print(i, end=" ")