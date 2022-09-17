n = int(input())
list = []
for i in range(n):
    a = int(input())
    list.append(a)
for i in list[::-1]:
    print(i,end=' ')