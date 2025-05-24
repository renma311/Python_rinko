#2桁を取り出す
def divide2(numbers):    
    list1to99.append(numbers[0:2])
    numbers = numbers[2:]
    return numbers

#１桁を取り出す
def divide1(numbers):
    list1to99.append(numbers[0])
    numbers = numbers[1:]
    return numbers

#1~99に分割する関数
def divide(numbers):
    #分割が終了したとき
    if len(numbers) == 0:
        print(list1to99)
        return 1
    
    #文字が残り１つのとき
    elif(len(numbers) == 1):
        if((numbers[0] not in list1to99) and (numbers[0] != '0')):
            if divide(divide1(numbers)):
                return 1
        
    
    else:
        #先頭が0ではないとき
        if(numbers[0] != '0'):
            #上２桁が既出でないとき
            if(numbers[0:2] not in list1to99):
                if divide(divide2(numbers)):
                    return 1
            
            #上１桁が既出でないとき
            if(numbers[0] not in list1to99): 
                if divide(divide1(numbers)):
                    return 1
    
    #print(numbers)
    #print(list1to99)
    #リストの先頭の値を文字列に戻す    
    numbers = list1to99.pop() + numbers
    return 0

if __name__ == '__main__':
    numbers = input()
    list1to99 = []
    divide(numbers)