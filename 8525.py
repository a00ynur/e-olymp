n = int(input())
matrix = [list(map(int,input().split())) for i in range(n)]
say = 0
cem = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]<0 and matrix[i][j] % 2 == 0:
            cem += matrix[i][j]
            say += 1
print(say,cem)