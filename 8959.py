count = input()
list = [int(i) for i in input().split()]

max = list[0]
min = list[0]

for j in list:
    if j > max:
        max = j

    if j < min:
        min = j

print(max - min)