number = int(input())
count = 1
while number // 10 > 0:
    number = number // 10
    count = count + 1
print(count)