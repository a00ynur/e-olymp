n = int(input())
say = 0
while n > 0:
    m = n % 10
    if m % 2 != 0:
        say = say + 1
    n = n // 10
    
print(say)