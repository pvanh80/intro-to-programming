# Course name: Intro to Programming
# Auto - Car
# Phan Viet Anh, 256296

# Fill in all TODOs in this file

from math import sqrt


# This is a text-based menu. You should ONLY touch TODOs inside the menu.
# TODOs in the menu call functions that you have implemented and take care
# of the return values of the function calls.

def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " + \
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    MENU_TEXT = "1) Fill 2) Drive 3) Quit \n-> "

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input(MENU_TEXT)

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            x, y, gas = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently
#
# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
#
# The function does not print anything and does not ask for any
# input.
def fill(size_gas, requested_gas, current_gas):
    if requested_gas >= size_gas:
        current_gas = size_gas
        return current_gas
    else:
        current_gas = requested_gas
        return requested_gas


# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car
#
# The parameters have to be in this order.
# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
#
# The return values have to be in this order.
# The function does not print anything and does not ask for any
# input.
def drive(x, y, new_x, new_y, current_gas, consumpted_100_gas):
    # It might be usefull to make one or two helper functions to help
    # the implementation of this function (drive)
    m = sqrt((new_x - x) * (new_x - x) + (new_y - y) * (new_y - y))
    p = (current_gas / consumpted_100_gas) * 100
    gas_after_driving = current_gas - (m / 100) * consumpted_100_gas
    if m <= p:
        if gas_after_driving <= 0:
            gas_after_driving = 0
        return new_x, new_y, gas_after_driving
    else:
        return coordinate_stop_point(x, y, new_x, new_y, current_gas, consumpted_100_gas)


# self - implementated functions
def coordinate_stop_point(x, y, new_x, new_y, current_gas, consumpted_100_gas):
    p = (current_gas / consumpted_100_gas) * 100
    m = distance_move(x, y, new_x, new_y)

    x_stop = x + p * (new_x - x) / m
    y_stop = y + p * (new_y - y) / m

    gas_after_driving = current_gas - (m / 100) * consumpted_100_gas
    if gas_after_driving <= 0:
        gas_after_driving = 0
    return x_stop, y_stop, gas_after_driving
    # Implement your own functions here. It is required to implement at least
    # two functions that take at least one parameter and return at least one
    # value.
    # The functions have to be used somewhere in the program.


def distance_move(x, y, new_x, new_y):
    return sqrt((new_x - x) * (new_x - x) + (new_y - y) * (new_y - y))


def read_number(prompt, error_message="Incorrect input!"):
    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


main()
