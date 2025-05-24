list_num = []
for i in range (1, int(input()) + 1):
    num = ''
    if(i % 3 == 0):
        num += 'F'
    

    if(i % 5 == 0):
        num += 'B'
    
    else:  
        if num != 'F':
            num = i 

    list_num.append(num)
print(list_num)