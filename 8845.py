n = int(input())
teklik = n % 10
onluq = n // 10 % 10
yuzluk = n // 100 % 10
yeni_eded = (n//1000)*100
print(yeni_eded + 10*onluq + teklik)