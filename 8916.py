list = []
n = int(input())
number = 0

for i in range(0, n):
	number += 2
	list.append(number)

print(*list, end=" ")