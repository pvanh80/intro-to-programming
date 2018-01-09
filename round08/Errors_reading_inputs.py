# Intro to programming
# Errors in reading the inputs
# Phan viet Anh
# 256296


def read_input(value):
    try:
        
        return int(input(value))

    except ValueError as e:

        return read_input(value)


def print_box(width, height, mark):

    index = 1

    while index <= height:
        print(width * mark)
        index += 1


def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


main()
