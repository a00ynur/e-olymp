n = int(input())
a = n//100
b = n//10%10
c = n%10
x1 = 100*a + 10*b + c
x2 = 100*a + 10*c + b
x3 = 100*b + 10*a + c
x4 = 100*b + 10*c + a
x5 = 100*c + 10*b + a
x6 = 100*c + 10*a + b

minx = 1000
maxx = 0
if x1 >= 100 and x1 < minx:
    minx = x1
if x2 >= 100 and x2 < minx:
    minx = x2
if x3 >= 100 and x3 < minx:
    minx = x3
if x4 >= 100 and x4 < minx:
    minx = x4
if x5 >= 100 and x5 < minx:
    minx = x5
if x6 >= 100 and x6 < minx:
    minx = x6

if x1 >= 100 and x1>maxx:
    maxx = x1
if x2 >= 100 and x2>maxx:
    maxx = x2
if x3 >= 100 and x3>maxx:
    maxx = x3
if x4 >= 100 and x4>maxx:
    maxx = x4
if x5 >= 100 and x5>maxx:
    maxx = x5
if x6 >= 100 and x6>maxx:
    maxx = x6
print(minx+maxx)