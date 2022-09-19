n = int(input())
product = 1

for i in str(n):
    if int(i) != 0:
        product = product * int(i)

print(product)