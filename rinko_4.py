import os
from collections import deque

#パスを受け取る
path = 'C:/Users/sugar/Downloads/rinko'
word_list = []
for root, dirs, files in os.walk(path):
    for filename in files:
        word_list.append(filename)   

start_word = input()    

queue = deque([(start_word.lower(), [start_word.lower()])]) 
shortest_path = [start_word for i in range(1000)]  
dist = [-1] * len(word_list) 

while queue:
    dist = [-1] * len(word_list) 
    word_now, visited = queue.popleft()
    for word in visited:
        if(word in word_list):  
            dist[word_list.index(word)] = visited.index(word)
    
    next_word_list = []
    for word in word_list:
        if dist[word_list.index(word)] == -1 and word[0].lower() == word_now[-1].lower():
            next_word_list.append(word)

    #print(visited)
    #print(next_word_list)
    
    if next_word_list:
        for next_word in next_word_list:
            tmp1 = visited + [next_word]
            queue.append((next_word, tmp1))                                       
                                               
    else:
        if max(dist) <= len(shortest_path):
            shortest_path = visited[1:len(visited)]                  
        if len(shortest_path) < max(dist):        
            break
        
print(shortest_path) 