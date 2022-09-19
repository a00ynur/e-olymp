n, m, k = map(int,input().split())
if n + m > k and k + m > n and n + k > m:
    print("YES")
else:
    print("NO")