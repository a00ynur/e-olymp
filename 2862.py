number = int(input())
bolen_sayi = 0
for i in range(1,number+1):
    if number % i==0:
        bolen_sayi = bolen_sayi +1 
print(bolen_sayi)