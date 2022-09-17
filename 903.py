n=int(input())

if n//100 > n%10:
    print(n//100)
elif n//100 < n%10:
    print(n%10)
else:
    print('=')