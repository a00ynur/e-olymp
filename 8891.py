n = int(input())
if n % 2==0:
    if n >= 0 or n % 3 != 0:
        print('YES')
    else:
        print('NO')
else:
    if n < 0 and n % 3 == 0:
        print('YES')
    else:
        print('NO')