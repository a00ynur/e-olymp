number = int(input())
count= 0 
while number!= 1:
    if number % 2 == 0:
        number = number / 2
        count = count + 1
    else:
        number = number + 1
        count = count + 1
print(count)