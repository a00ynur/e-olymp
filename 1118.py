num = int(input())
if num <= 1:
    print('Ooops!')
else:
    numeral = list(map(int, input().split()))

    print(min(numeral),max(numeral))