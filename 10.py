pail = 0
day = 0
count = int(input())
i = count

while(pail <= 0.5):
    pail = pail + 1/i
    day += 1
    i = i - 1

print(count - day + 1)