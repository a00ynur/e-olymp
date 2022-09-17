a, b, c = map(int,input().split())
diskriminant = b**2-(4*a*c)
if diskriminant <0:
    print('No roots')
elif diskriminant==0:
    x=-(b/(2*a))
    print('One root:', int(x))
else:
    x1=((-b)+diskriminant**0.5)/(2*a)
    x2=((-b)-diskriminant**0.5)/(2*a)
    if x1<x2:
        print('Two roots:', int(x1), int(x2))
    elif x1==x2:
        print('One root:', int(x1))
    else:
        print('Two roots:', int(x2), int(x1))