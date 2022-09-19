number = int(input())
list = list(map(int,input().split()))
max_number = max(list)
count = 0

for i in list:
	if i == max_number:
	    count = count + 1

print(count)