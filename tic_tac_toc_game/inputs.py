
def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:").strip())
            return num
        except ValueError as error:
            print(f"{error},try again!")
            
