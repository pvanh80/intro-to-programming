import math

PI = math.pi


def circumference_squre(a):
    return 4 * a


def circumference_rec(a, b):
    return (a + b) * 2


def surface_area_square(a):
    return a * a


def surface_area_rec(a, b):
    return a * b


def circumference_circle(a):
    return 2 * a * PI


def surface_area_cir(a):
    return a * a * PI


def main():
    while True:
        letter_in = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if letter_in == "s":
            while True:
                a = input("Enter the length of the square's side: ")
                if a.replace(".", "", 1).isdigit():
                    if float(a) > 0:
                        break

            print("The total circumference is", format(circumference_squre(float(a)), '.2f'))
            print("The surface area is", format(surface_area_square(float(a)), '.2f'))
            print()

        elif letter_in == "r":
            while True:
                a = input("Enter the length of the rectangle's side 1: ")
                if a.replace(".", "", 1).isdigit():
                    if float(a) > 0:
                        break
            while True:
                b = input("Enter the length of the rectangle's side 2: ")
                if b.replace(".", "", 1).isdigit():
                    if float(b) > 0:
                        break

            print("The total circumference is", format(circumference_rec(float(a), float(b)), '.2f'))
            print("The surface area is", format(surface_area_rec(float(a), float(b)), '.2f'))
            print()
        elif letter_in == "c":
            while True:
                a = input("Enter the circle's radius: ")
                if a.replace(".", "", 1).isdigit():
                    if float(a) > 0:
                        break
            print("The total circumference is ", format(circumference_circle(float(a)), '.2f'))
            print("The surface area is ", format(surface_area_cir(float(a)), '.2f'))
            print()
        elif letter_in == "q":
            print("Goodbye!")
            break

        else:
            print("Incorrect entry, try again!")
            print()


main()