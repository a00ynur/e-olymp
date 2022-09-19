n = int(input()) #135
first = n // 10  #13
second = (n // 100) * 10 + n % 10  #15
third = n % 100 #35
print(max(first, second, third ))