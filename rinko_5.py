def track(maze):
    draw = ""
    for x in range(len(maze)-2):
        for y in range(len(maze[x])-2):
            if maze[x+1][y+1] == 's':
                draw += "s "    #スタート
            if maze[x+1][y+1] == 'X':
                draw += "X "    #壁
            elif maze[x+1][y+1] == '+':
                draw += "+ "    #探索済みの道
            elif maze[x+1][y+1] == 'g':
                draw += "g "   #ゴール位置
            elif maze[x+1][y+1] == ' ':
                draw += "  "    #未探索の道

        draw += "\n"
    print(draw)

def Maze(x, y):
    #ゴールについた時点で終了
    if maze[x][y] == 'g':
        track(maze)
        exit()

    #探索済みとしてセット
    maze[x][y] = '+'

    #現在位置の上下左右を探索：
    if ((maze[x-1][y] != '+') and (maze[x-1][y] != 'X') and (maze[x-1][y] != 's')):#左
        Maze(x-1, y)
    if ((maze[x+1][y] != '+') and (maze[x+1][y] != 'X') and (maze[x+1][y] != 's')):#右
        Maze(x+1, y)
    if ((maze[x][y-1] != '+') and (maze[x][y-1] != 'X') and (maze[x][y-1] != 's')):#上
        Maze(x, y-1)
    if ((maze[x][y+1] != '+') and (maze[x][y+1] != 'X') and (maze[x][y+1] != 's')):#下
        Maze(x, y+1)

    maze[x][y] = ' '
    return -1

if __name__ == '__main__':
    #迷路作成
    keiro = input()
    space = 0
    cnt = 0
    yoko_tate = ''
    for i in keiro:     #数字のみを取り出す
        if i == 'X':
            break
        if i == 's':
            break
        if i == 'g':
            break
        if(i == ' ') and (space != 0):
            break
        if(i == ' ') and (space == 0):
            space += 1   

        yoko_tate += i
        cnt += 1

    #縦と横の大きさを取り出す
    yoko_tate_list = yoko_tate.split()
    yoko = int(yoko_tate_list[0])
    tate = int(yoko_tate_list[1])

    #迷路をリスト化
    meiro_list = list(keiro)
    del meiro_list[0:cnt]

    #横一列をリストとしてリストのリストを作る[[横一列][横一列][横一列]...[横一列]]
    #その後作ったリストの外枠を'X'で囲む（外に出ないようにするため）
    maze = [['X' for i in range(yoko+2)]]
    meiro = []
    for i in range(tate):
        a = ['X']
        for j in meiro_list[yoko*i:yoko*i+yoko]:
            a.append(j)
        a.append('X')
        maze.append(a)
    maze.append(maze[0])

    #スタートの位置特定
    start_tate = 0
    for i in maze:
        start_yoko = 0
        start_tate += 1
        for j in i:
            start_yoko += 1
            if j == 's':
                break
        else:
            continue
        break
        
    #探索
    result = Maze(start_yoko, start_tate)  
    #print(meiro_list)
    #print(yoko_tate_list)
    #print(meiro)
    #print(maze)
    #print(start_yoko,start_tate)
    