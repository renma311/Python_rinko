str1 = input()
s = list (str1)
a1 = [] #\の番地を要素とするリスト
a2 = [] #\の番地と高さが同じ部分の池の面積のリストを要素とするリスト [[番地,面積]]
cnt = 0 #左から数えて何番目か
sum = 0 #池の面積
total = []
for i in s:
    if i == '\\':
        a1.append(cnt) #\の番地をリストに入れる
    elif i == '/' and a1:
        j = a1.pop() 
        l = cnt - j #横1列の池の面積を出す
        
        while (a2 and j < a2[-1][0]): #while文の中でつながっている池の面積を足す
            l += a2.pop()[1]
        a2.append([j, l]) 
    cnt += 1

for k in a2:
    sum += k[1]
    total.append(k[1])

print(sum)
print(*total)