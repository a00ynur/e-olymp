n, m, x, y = map(int, input().split())
matrix = [[0] * m for i in range(n)]

element = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = element
            element += 1
    else:
        for j in range(m-1, -1, -1):
            matrix[i][j] = element
            element += 1

print(matrix[x-1][y-1])