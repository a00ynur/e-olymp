num = input()
hasil = 1
index = 1
for i in num:
    if(i == "-"):
        index -= 1
    if(index % 2 != 0):
        hasil *= int(i)
    index += 1
print(hasil)