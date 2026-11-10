from db.board import BOARD,WINNING_LINES
from tic_tac_toc_game.inputs import get_num
from tic_tac_toc_game.validates import is_not_empty,is_in_range
from tic_tac_toc_game.manage_game import check_draw,check_win,update_board,check_if_index_empty
from tic_tac_toc_game.result import shaw_board,print_draw_msg,print_winning_msg
def main():
    sing = "X"
    while True:
        shaw_board(BOARD)
        num = get_num(f"player {sing} enter your choice(1-9)")
        if check_if_index_empty(BOARD,num):
            update_board(BOARD,num,sing)
        else:
            continue
        if check_win(BOARD,WINNING_LINES,sing):
            print_winning_msg(sing)
            shaw_board(BOARD)
            break
        elif check_draw(BOARD):
            print_draw_msg()
            shaw_board(BOARD)
            break
        sing = "O" if sing == "X" else "X"

if __name__ == "__main__":
    main()