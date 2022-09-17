n = int(input())
matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i+j < n-1:
            matrix[i][j] = 2
        elif i+j > n-1:
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='')
    print()