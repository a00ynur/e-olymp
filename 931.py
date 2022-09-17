number = input()
sum = 0
product = 1
for i in number:
    i=int(i)
    sum = sum + i 
    product = product * i 
number = int(number)
a = float(product / sum)
print("{:.3f}".format(a))