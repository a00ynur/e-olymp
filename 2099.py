n = int(input())
arr1 = list(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))

arr3 = []

for i in arr1:
    for j in arr2:
        if i == j:
             break
    else:
        arr3.append(i)
print(len(arr3))
print(*arr3)