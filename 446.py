number = int(input())
count = 0
while(number >= 1):
    for i in range(1,number + 1):
        residue = number % i
        total = number // i
        if residue == total :
            count = count + 1
    print(count)
    break