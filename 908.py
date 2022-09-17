numbers = int(input())  #ededlern sayi
number =input().split()  #ededlerin ozu
line=[]
line1=[]
for i in number:
    i=int(i)
    if i>0:
        line.append(i)
for i in line:
    if i%6==0:
        line1.append(i)
print(len(line1),sum(line1))