n = int(input())
l = list(map(int, input().split()))
maximum_1 = -101
maximum_2 = -101
for i in range(n):
    if l[i] > maximum_1:
        l.append(maximum_1)
        maximum_1 = l[i]
l.remove(maximum_1)
for i in range(n-1):
    if l[i] > maximum_2:
        l.append(maximum_2)
        maximum_2 = l[i]
print(maximum_1 + maximum_2)