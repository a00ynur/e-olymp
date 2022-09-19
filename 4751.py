n = int(input())
matrix = [list(map(int,input().split())) for i in range(n)]
esas = 0
ters = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            esas += matrix[i][j]
        if i+j == n-1:
            ters += matrix[i][j]
print(esas,ters)