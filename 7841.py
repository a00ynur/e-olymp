n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    if l[i] % 2 == 1:
        print(l[i], end= " ")