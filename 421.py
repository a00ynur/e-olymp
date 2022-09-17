n,k = map(int,input().split())
sum = 0
n = n/ k
while n > 1:
    sum = sum + 1
    n = n/ k
print(sum )