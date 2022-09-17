a, b, c = map(int, input().split())
V = a * b * c
m = V * 6 #butun uzlerin sayi
n = 2 * (a * b + a * c + b * c)  #lazim olan uzler
result = m - n 
print (V, result)