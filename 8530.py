n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
a,b=map(int,input().split())
for i in range(a):
    for j in range(b):
        print(l[i][j], end=' ')
    print()