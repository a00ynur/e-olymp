n=int(input())
l = list(map(int,input().split()))
cem=0
for i in l:
    if i<max(l):
        cem+=i
print(cem)