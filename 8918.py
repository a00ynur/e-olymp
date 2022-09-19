list = []
n = int(input())

for i in range(1, n+1):
	i = i ** 2
	list.append(i)

print(*list, end=" ")