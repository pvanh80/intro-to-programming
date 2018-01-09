# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Template for task: ruutu
def print_box(w, h, m):
    i = 1
    while i <= h:
        print(w * m)
        i += 1


def main():
    width = int(input("Enter the width for a box: "))
    height = int(input("Enter the height for a box: "))
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


main()
