n, m, k = map(int,input().split())
room = n // k + m // k 
if n % k != 0:
    room = room + 1
if m % k != 0:
    room = room + 1
print(room)