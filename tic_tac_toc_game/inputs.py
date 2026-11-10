from tic_tac_toc_game.validates import is_not_empty,is_in_range
def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:").strip())
            if is_in_range(num) and is_not_empty(num):
                return num
        except ValueError as error:
            print(f"{error},try again!")

