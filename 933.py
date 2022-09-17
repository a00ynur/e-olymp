n=int(input())
if n<0:
    n=-n
    number1 = (n//10)
    number2 = n%10

else:
  number1 = n//10
  number2 = (n%10)
print(number1+number2)