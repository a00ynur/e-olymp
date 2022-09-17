sentence = input()
sentence = sentence.replace(" ","")
reverse = sentence[::-1]

if sentence == reverse:
    print("YES")
else:
    print("NO")