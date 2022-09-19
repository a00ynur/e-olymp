n = int(input())
k = 0
import math

for i in range (2, math.isqrt(n)+1):
    if n % i ==0:
        k = k + 1
        break
if k>0:
    print("0")
else:
    print("1")