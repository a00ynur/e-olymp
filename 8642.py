n = input().split()
b = int(n[0])
c = int(n[1])

for i in range(b,c+1):
    if i == (((i//1000)**4)+(((i//100)%10)**4)+(((i%100)//10)**4)+((i%10)**4)):
        print(i, end=' ')