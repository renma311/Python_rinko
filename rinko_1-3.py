def FizzBuzz(i):
    num = ''
    if(i % 3 == 0):
        num += 'F'
    

    if(i % 5 == 0):
        num += 'B'
    
    else:  
        if num != 'F':
            num = i 
    return num

list1 = []
for i in range (1, int(input()) + 1):
    list1.append(i)

print (list(map(FizzBuzz, list1)))