n=input().split()

a = int(n[0])
h = int(n[1])
S = (1/2*a*((h*h+(1/4)*a*a)**0.5))*4+a*a
print("{:.1f}".format(S))