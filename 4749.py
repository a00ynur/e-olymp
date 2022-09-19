n,m = map(int,input().split())
qiymet = [list(map(int,input().split())) for i in range(n)]
bosh = input()
bilet = [list(map(int,input().split())) for i in range(n)]
cem = 0
for i in range(n):
    for j in range(m):
        if bilet[i][j] == 1:
            cem += qiymet[i][j]
print(cem)