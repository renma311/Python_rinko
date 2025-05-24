list_num = []
for i in range (1, int(input()) + 1):
    num = ''
    if( 3 * (i // 3) == i):
        num += 'F'
    

    if( 5 * (i // 5) == i):
        num += 'B'
    
    else:  
        if num != 'F':
            num = i 
    list_num.append(num)
print(list_num)