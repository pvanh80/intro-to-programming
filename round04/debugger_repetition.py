# TIE-02106 Introduction to Programming
# Program code template for testing the use of a debugger

def main():

    line = input("How many Fibonacci numbers do you want: ")
    how_many = int(line)

    old = 0
    now = 1
    line_number = 1

    while line_number <= how_many:
        print(line_number, ". ", now, sep="")
        new = old + now
        now = new
        old = now

        line_number += 1


main()
