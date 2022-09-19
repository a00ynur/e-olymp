n, m = map(int, input().split()) 

matrix = [list(map(int, input().split())) for i in range(n)]

new_matrix = [[0] * m for i in range(n)]

for i in range(n):
    new_j = 0
    for j in range(m):
        if matrix[i][j] != 0:
            new_matrix[i][new_j] = matrix[i][j]
            new_j += 1

for i in new_matrix:
    print(*i)