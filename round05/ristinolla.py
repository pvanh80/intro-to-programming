# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: ristinolla, program code template


def print_two_dimensional_list(game_board):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in game_board]))


def main():
    # TODO: implement the datastructure for storing the board
    game_board = [[".", ".", "."],
                  [".", ".", "."],
                  [".", ".", "."]
                  ]
    turns = 0  # How many turns have been played

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
            x = int(x)
            y = int(y)
            if game_board[y][x] == ".":
                game_board[y][x] = mark
                print_two_dimensional_list(game_board)
                turns += 1
            else:
                print("Error: a mark has already been placed on this square.")
                # TODO: implement the turn of one player here

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
