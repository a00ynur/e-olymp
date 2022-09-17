import math
n=input().split(' ')
x1 = float(n[0])
y1 = float(n[1])
r1 = float(n[2])
x2 = float(n[3])
y2 = float(n[4])
r2 = float(n[5])
number = 0
if x1==x2 and y1==y2:
    if r1==r2:
        number = -1
    else:
        number = 0
else:
    a = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if a==r1+r2 or a==math.fabs(r1-r2):
        number = 1
    else:
        if a>(r1+r2) or a+r2<r1:
            number = 0
        else:
            number = 2
print(number)