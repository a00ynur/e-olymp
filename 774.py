r, w, l = map(int, input().split())
diametr = 2 * r
if(diametr >= (w ** 2 + l ** 2)**0.5):
    print("YES")
else:
    print("NO")