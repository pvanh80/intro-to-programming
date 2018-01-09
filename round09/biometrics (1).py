# Introduction to Programming K2017
# Biometric Recognition
# Phan Viet Anh
# 256296

###############################################################################
# read_biometric_registry(filename)                                                     
# =========================================
# Function reads the biometric information from the file whose name is in
# the parameter filename. The read information will be parsed and saved in 
# the data structure that is in the variable called result. The coder has
# to define the data structure by him/herself.
# After successfully reading the file and saving its contents in the data
# structure, the function returns the result. If there's an error, None is
# returned.
#         
# PLEASE NOTE:
# (a) Implement all parts of the code that say TODO.
# (b) The data structure returned by the function must be something that
#     that nests lists and/or dicts. That is the wole point of this project:
#     to use nested data structures.
###############################################################################

from math import pow,sqrt


def read_biometric_registry(filename):
    result = []  # initialize your data structure here
    passport_name = []
    handled_passports = []

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                row = row.rstrip()

                fields = row.split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields in the file:")
                    print("'", row, "'", sep="")
                    return None

                for ind in range(3, 8):
                    fields[ind] = float(fields[ind])
                    if not (0 <= fields[ind] <= 3.0):
                        print("Error: there is a erroneous value in the file:")
                        print("'", row, "'", sep="")
                        return None

                name = fields[0] + ", " + fields[1]
                passport = fields[2]
                biometric = fields[3:]

                if passport in handled_passports:
                    print("Error: passport number", passport, "found multiple times.")
                    return None

                else:
                    handled_passports.append(passport)

                #TODO:
                #save the read information in the result data structure

                passport_name.append(name)
                passport_name.append(passport)

                for element in biometric:
                    passport_name.append(element)

                result.append(passport_name)
                passport_name = []

        return result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")

    except ValueError:
        print("Error: there's a non-numeric value on row:")
        print("'", row, "'", sep="")

    return None


###############################################################################
# TODO
###############################################################################
def execute_match(registry):
    # TODO
    match = False
    result = []
    matched_list = []
    variance = 0.1
    for key in range(len(registry)):

        for element in range(len(registry)):

            square_root = pow((float(registry[key][2]) - float(registry[element][2])), 2) \
                          + pow((float(registry[key][3]) - float(registry[element][3])), 2) \
                          + pow((float(registry[key][4]) - float(registry[element][4])), 2) \
                          + pow((float(registry[key][5]) - float(registry[element][5])), 2) \
                          + pow((float(registry[key][6]) - float(registry[element][6])), 2)
            if sqrt(square_root) < variance:

                result.append(registry[element])
                # del registry[element]

        if len(result) > 1 and result not in matched_list:
            match = True
            matched_list.append(result)

        result = []
    if match == False :
        print('No matching persons were found.')
    for sub_matched in matched_list:
           print('Probably the same person:')
           for people in sub_matched:
               print(people[0], people[1], format(people[2], '.2f'),
                     format(people[3], '.2f'),
                     format(people[4], '.2f'),
                     format(people[5], '.2f'),
                     format(people[6], '.2f'),
                     sep=';')
           print()

###############################################################################
# TODO
###############################################################################
def execute_search(registry):
    # TODO

    result = []
    variance = 0.1
    biometric = ''
    while True:
        biometric = input("enter 5 measurement points separated by semicolon: ")
        biometric_values = biometric.split(';')
        if biometric == '':
            print('Error: Empty input. Try again.')
        elif len(biometric_values) < 5:
            print('Error: wrong number of measurements. Try again.')
        else:
            try:
                for value in biometric_values:
                    float(value)
                break
            except :
                print('Error: enter floats only. Try again.')

    for key in registry:

        square_root = pow((float(biometric_values[0]) - float(key[2])),2)\
                        + pow((float(biometric_values[1]) - float(key[3])), 2) \
                        + pow((float(biometric_values[2]) - float(key[4])), 2)\
                        + pow((float(biometric_values[3]) - float(key[5])), 2)\
                        + pow((float(biometric_values[4]) - float(key[6])), 2)
        if sqrt(square_root) < variance :
            result.append(key)
    if len(result) > 0:
        print('Suspects found:')
        for element in result:
            print(element[0], element[1], format(element[2], '.2f'),
                  format(element[3], '.2f'),
                  format(element[4], '.2f'),
                  format(element[5], '.2f'),
                  format(element[6], '.2f'),
                  sep=';')
        print()
    else:
        print('No suspects were found.')
        print()



###############################################################################
# command_line_user_interface
# Very simple user interface. It might be good to add some helper functions.
#                                                                             
###############################################################################
def command_line_user_interface(registry):
    while True:
        command = input("command [search/match/<enter>] ")
        if command == "":
            return
        elif command == "match":
            execute_match(registry)
        elif command == "search":
            execute_search(registry)
        else:
            print("Error: unknown command '", command,
                  "': try again.", sep="")


###############################################################################
# main()                                                                      #
# ======                                                                      #
# Main program for the project. You're not supposed to edit this.
#
###############################################################################
def main():
    registry_file = input("Enter the name of the registry file: ")

    biometric_registry = read_biometric_registry(registry_file)
    #print(biometric_registry)
    if biometric_registry is not None:
        command_line_user_interface(biometric_registry)


main()
