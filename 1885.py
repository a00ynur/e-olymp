n = input()
X = 0
for i in n:
	if i == '-':
		X = X + 1
	elif i == '1':
		X = X + 2
	elif i == '0' or i == '6' or i == '9':
		X = X + 6
	elif i == '2' or i == '3' or i == '5':
		X = X + 5
	elif i == '4':
		X = X + 4
	elif i == '7':
		X = X + 3
	elif i == '8':
		X = X + 7
print(X)