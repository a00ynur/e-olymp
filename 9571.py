n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
print(sum)