n = int(input())
arr = list(map(int,input().split()))
arr1 = arr[-1:-2:-1] + arr[:len(arr)-1]
for i in range(len(arr1)):
    print(arr1[i], end= " ")