n = int(input())
teklik = n % 10
onluq = n // 10 % 10
yeni_eded = (n // 100) * 10
print(yeni_eded + teklik)
