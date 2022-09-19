n = int(input())
massiv = list(map(int,input().split()))
l = []
for i in range(n):
	if massiv[i] not in l:
		l.append(massiv[i])
if l:
	print(*l)
else:
	print('NO')