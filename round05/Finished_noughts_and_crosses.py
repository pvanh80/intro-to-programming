# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template

# for Caro game, just checking the five continuous point in row, col, and diagonal > winner of lose

def create_game_board(rows, cols):
    game_board = []
    main_game_board = []
    for row in range(rows):
        game_board.append(".")

    for col in range(cols):
        main_game_board.append(game_board)

    return main_game_board


def print_two_dimensional_list(game_board):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in game_board]))


def checking_win_lose_row(row, game_board, mark):
    count = 0
    for cols in range(len(game_board)):
        if game_board[row][cols] == mark:
            count += 1
    return count


def checking_win_lose_col(col, game_board, mark):
    count = 0
    for row in range(len(game_board)):
        if game_board[row][col] == mark:
            count += 1

    return count


def checking_disgonal_line(game_board, mark):
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == mark or game_board[0][0] == game_board[1][1] == \
            game_board[2][2] == mark:
        return True
    else:
        return False


def main():
    ROWS = 10
    COLS = 10
    # TODO: implement the datastructure for storing the board
    game_board = create_game_board(ROWS, COLS)
    turns = 0  # How many turns have been played
    draw = 1
    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.
    print_two_dimensional_list(game_board)
    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)  # col
            y = int(y)  # row

            if game_board[y][x] == ".":
                game_board[y][x] = mark
                print_two_dimensional_list(game_board)
                if (checking_win_lose_row(y, game_board, mark)) == 3:
                    print("The game ended, the winner is " + mark)
                    draw = 0
                    break
                if (checking_win_lose_col(x, game_board, mark)) == 3:
                    print("The game ended, the winner is " + mark)
                    draw = 0
                    break
                if checking_disgonal_line(game_board, mark):
                    print("The game ended, the winner is " + mark)
                    draw = 0
                    break
                turns += 1
            else:
                print("Error: a mark has already been placed on this square.")
                # TODO: implement the turn of one player here

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")
    if draw == 1: print("Draw!")


main()
