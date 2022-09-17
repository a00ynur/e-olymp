number = input()
degreeSymmetry = 0
count = len(number)
period = count // 2
for i in range (0, period):
    if number[i] == number[count-(i+1)]:
        degreeSymmetry =  degreeSymmetry + 1
if count % 2 != 0:
     degreeSymmetry =  degreeSymmetry + 1
print( degreeSymmetry)