n = int(input()) 
right= n // 1000
left = n % 1000
a = left // 100
b = left // 10 % 10
c = left % 10
new_n = right* 1000 + b * 100 + a*10 + c
print(new_n)