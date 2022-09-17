n = int(input())
if n < 0: 
    n = -n 
a = int(input())
number = 0

while n>0:
    m = n % 10
    if m == a:
        number += 1
    n = n // 10
print(number)