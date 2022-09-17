n = int(input())
m = list(map(int,input().split()))
for i in range(n):
    if m[i] >= 0:
        print(m[i]+2, end=" ")
    else:
        print(m[i], end= " ")