#3:Apple 5:Orange 9:Banana 18
list_num = []
input1 = str(input())
x = input1.split()
count = int(x.pop())
y = []

for j in x:
    y.append(j.split(':'))

for i in range (1, count + 1):
    num = ''
    for k in y:
        if  i % int(k[0]) == 0:
             num += k[1]
    if(num == ''):
        num = i
    list_num.append(num)
print(list_num)
