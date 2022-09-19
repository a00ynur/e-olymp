n = input()
ikiler = n.count('2')
besler = n.count('5')
if ikiler == besler:
    print('=')
elif ikiler < besler:
    print(5)
else:
    print(2)