board_val = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]


def draw_board(val1, val2, val3, val4, val5, val6, val7, val8, val9):
    board = f"""
              |          |
        {val1}     |     {val2}    |     {val3}
              |          |
    ----------|----------|----------
              |          |
        {val4}     |     {val5}    |     {val6}
              |          |
    ----------|----------|----------
              |          |
        {val7}     |     {val8}    |     {val9}
              |          |
    """
    return board


is_user_one = True
game_over = False

user1 = 0
user2 = 0


def is_winner(brd):
    board = brd
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    elif board[1][0] == board[1][1] == board[1][2] != " ":
        return True
    elif board[2][0] == board[2][1] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][0] == board[2][0] != " ":
        return True
    elif board[0][1] == board[1][1] == board[2][1] != " ":
        return True
    elif board[0][2] == board[1][2] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    else:
        return False


def is_full(brd):
    for row in brd:
        for elem in row:
            if elem == " ":
                return False
    return True


def clear_board():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def score(u1, u2):
    print(f"""       Points      
user1: {u1}             user2: {u2}""")


print(draw_board(1, 2, 3, 4, 5, 6, 7, 8, 9))


while not game_over:
    user_input = input("enter box number: ")
    try:
        user_input = int(user_input) - 1
        first = user_input // 3
        second = user_input - first * 3
    except IndexError:
        print("Please enter two numbers. One for rows, second for columns")
        continue
    except ValueError:
        print("Please enter numbers only")
        continue
    if is_user_one:
        try:
            if board_val[first][second] == " ":
                board_val[first][second] = "X"
            else:
                print("box is already filled, please try again!")
                continue
        except IndexError:
            print("wrong index, out of range, please try again!")
            continue
        print(draw_board(board_val[0][0], board_val[0][1], board_val[0][2], board_val[1][0], board_val[1][1],
                         board_val[1][2], board_val[2][0], board_val[2][1], board_val[2][2]))
        if is_winner(board_val):
            print("X is a winner")
            user1 += 1
            score(user1, user2)
            yn = input("do you want to play again? y/n: ")
            if yn == "y" or yn == "yes":
                board_val = clear_board()
                is_user_one = True
                print(draw_board(board_val[0][0], board_val[0][1], board_val[0][2], board_val[1][0], board_val[1][1],
                                 board_val[1][2], board_val[2][0], board_val[2][1], board_val[2][2]))
                continue
            else:
                break
        is_user_one = False
        if is_full(board_val):
            print("it's a tie, game over")
            yn = input("do you want to play again? y/n: ")
            if yn == "y" or yn == "yes":
                board_val = clear_board()
                is_user_one = True
                print(draw_board(board_val[0][0], board_val[0][1], board_val[0][2], board_val[1][0], board_val[1][1],
                                 board_val[1][2], board_val[2][0], board_val[2][1], board_val[2][2]))
                continue
            else:
                break

        continue
    else:
        try:
            if board_val[first][second] == " ":
                board_val[first][second] = "O"
            else:
                print("box is already filled, please try again!")
                continue
        except IndexError:
            print("wrong index, out of range, please try again!")
            continue
        print(draw_board(board_val[0][0], board_val[0][1], board_val[0][2], board_val[1][0], board_val[1][1],
                         board_val[1][2], board_val[2][0], board_val[2][1], board_val[2][2]))
        if is_winner(board_val):
            print("O is a winner")
            user2 += 1
            score(user1, user2)
            yn = input("do you want to play again? y/n: ")
            if yn == "y" or yn == "yes":
                board_val = clear_board()
                is_user_one = True
                print(draw_board(board_val[0][0], board_val[0][1], board_val[0][2], board_val[1][0], board_val[1][1],
                                 board_val[1][2], board_val[2][0], board_val[2][1], board_val[2][2]))
                continue
            else:
                break
        is_user_one = True
        continue
