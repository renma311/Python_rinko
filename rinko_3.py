def print_board(board):
    size = len(board)
    for i in range(size):
        if i > 0: print() 
        for j in range(size):
            print("{0: 4d}".format(board[i][j]), end = ' ')
    print()
    return

def tour(board, x, y, cnt):
    size = len(board)
    if(x < 0 or x >= size): return
    if(y < 0 or y >= size): return
    if(board[x][y] != 0) : return
    
    board[x][y] = cnt + 1
    cnt += 1
    if(board[x][y] == size*size):
        print_board(board)
        #board[x][y] = 0
        return 
    z = [[-2,-1],[-2,1],[2,-1],[-2,-1],[1,-2],[1,2],[-1,-2],[-1,+2]]

    for a in z:
        tour(board, x+a[0],x+a[1],cnt)
    """
    tour(board, x-2, y-1, cnt)
    tour(board, x-2, y+1, cnt)
    tour(board, x+2, y-1, cnt)
    tour(board, x+2, y+1, cnt)
    tour(board, x-1, y-2, cnt)
    tour(board, x-1, y+2, cnt)
    tour(board, x+1, y-2, cnt)
    tour(board, x+1, y+2, cnt)
    """
    board[x][y] = 0
    return


n = int(input())
board = [[0 for x in range(n)] for y in range (n)]
tour(board, n-1, n-1, 0)