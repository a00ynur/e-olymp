h,w,l,k = [int(x) for x in input().split()]
v=h*w*l
if  v%k==0:
    print(v//k)
else:
    print(v//k+1)