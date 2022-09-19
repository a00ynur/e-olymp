n, m = map(int, input().split()) # 3 4

matrix1 = [[0] * m for i in range(n)]

element = 1

for i in range(n-1, -1, -1): # 2 1 0
    for j in range(m):
        matrix1[i][j] = element
        element += 1

matrix2 = [[0] * m for i in range(n)]

element = 1

for j in range(m):
    for i in range(n-1, -1, -1):
        matrix2[i][j] = element
        element += 1

count = 0

for i in range(n):
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            count += 1

print(count)