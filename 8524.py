n = int(input())
matrix = [list(map(int,input().split())) for i in range(n)]
cem = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0:
            cem += matrix[i][j]
print(cem)