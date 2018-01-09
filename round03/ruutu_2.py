# Johdatus ohjelmointiin
# Print a box with input checking


def read_input(str_value):
     value_in = int(input(str_value))
     while 1:
         if value_in > 0:
             break
         else:
             value_in = int(input(str_value))
     return value_in


def print_box(w,h,m):
    i = 1
    while i <= h:
        print(w * m)
        i += 1


def main():

    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width,height,mark)

main()

