n = int(input())
tax = n // 100

if n % 100 != 0:
   tax += 1
    
print(tax)