
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
