n = int(input())
tek = 0
cut = 0
x = True 
while n > 0:
    if  x:
        tek += n % 10
        x = False
    else:
        cut += n % 10
        x = True
    n //= 10
print(tek*cut)