n = int(input())
birler = 0
sifirlar = 0

for i in range(0, n):
    a = int(input())
    if a == 0:
        sifirlar += 1
    elif a == 1:
        birler += 1

if birler > sifirlar:
    print(sifirlar)

elif birler < sifirlar:
    print(birler)

else:
    print(birler)