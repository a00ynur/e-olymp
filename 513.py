n , m = map(int, input().split())
a = 1
if ( n >= m):
	print(0)
else:
	for i in range(2, n+1):
		a = (a * i ) % m
	print(a)