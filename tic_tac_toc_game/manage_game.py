
WINNING_LINES = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]]

def check_win(board,wining_list,sing):
    for row in wining_list:
        count = 0
        for i in row:
            if board[i] == sing:
                count +=1
            if count ==3:
                return True
    return False         
    

def check_draw(board):
    for i in board:
        if i !="X" and i !="O":
            return False
    return True                    

def check_if_index_empty(board,num):
    if board[num-1] == num:
        return True
    return False

def update_board(board,num,sing):
    board[num-1] = sing    
