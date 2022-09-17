import math
d, p = map(int,input().split())
S = d*(d+math.sqrt(4*p*p-d*d))
V =d*d*math.sqrt(p*p-d*d/2)/3
print("{:.3f}".format(S),end=" ")
print("{:.3f}".format(V))