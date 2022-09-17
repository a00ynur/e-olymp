num = input().split()
x = int(num[0])
y = int(num[1])
earth = 81/((x**2)+(y**2))
moon = 1/(((384000 - x)** 2)+(y**2))
if earth == moon:
    print("Equal")
elif earth > moon:
    print("Earth")
else:
    print("Moon")