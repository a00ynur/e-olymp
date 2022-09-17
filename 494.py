text = input()
count = 0 
for i in text:
    if i in ("A", "E", "I", "O", "U" , "Y"):
        count = count + 1
print(count)