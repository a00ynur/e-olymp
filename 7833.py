number = int(input())
list = list(map(int,input().split()))
count = 0
sum = 0
max_sum = 0
max_count = 0

for i in list:

    sum = sum + i
    count = count + 1

numerical_average = sum / count

for i in list:
    if i > numerical_average:
        max_sum = max_sum + i
        max_count = max_count + 1

print(max_sum, max_count)