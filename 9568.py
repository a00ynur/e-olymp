n, m = map(int, input().split()) #n=setir m=sutun 4 5

matrix = [list(map(int, input().split())) for i in range(n)]

new_matrix = [[0] * m for i in range(n)]

for i in range(m):
    new_j = n-1
    for j in range(n-1,-1,-1):
        if matrix[j][i] != 0:
            new_matrix[new_j][i] = matrix[j][i]
            new_j -= 1

for i in new_matrix:
    print(*i)