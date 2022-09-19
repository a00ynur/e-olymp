count = int(input())
for i in range(1, count +1):
    massiv1 = input()
    massiv2 = massiv1.split()
    price = float(massiv2[0])
    if price >= 3.5 and ("A"== massiv2[1] or "B" ==massiv2[1]):
        print(1)
    else :
        print(0)