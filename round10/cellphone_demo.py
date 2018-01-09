# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296

import pickle
from cellphone import CellPhone


def main():
    # cellphone_list = []
    #
    # man1 = input('What is your phone\'s manufacture? ')
    # mod1 = input('What is your phone\'s model? ')
    # price1 = float(input('What is your phone\'s price? '))
    # man2 = input('What is your phone\'s manufacture? ')
    # mod2 = input('What is your phone\'s model? ')
    # price2 = float(input('What is your phone\'s price? '))
    #
    # cellphone1 = CellPhone(man1, mod1, price1)
    # cellphone2 = CellPhone(man2, mod2, price2)
    #
    # #cellphone_list.append(cellphone)
    #
    # file = open('cellphone.dat', 'wb')
    #
    # pickle.dump(cellphone1,file)
    # pickle.dump(cellphone2,file)
    #
    # file.close()
    #
    # Read file from cellphone

    cellphone_list = []

    # file = open('cellphone.dat','rb')
    #
    # cellphone_list = pickle.load(file)
    #
    # for cellphone in cellphone_list:
    #     print(cellphone.get_manufact())


    # list_example = [1, 2, 4, 5]
    # list_example2 = [6, 7, 8, 9]
    big_content = []
    end_of_file = False
    file = open('cellphone.dat','rb')
    while not end_of_file:
        try:
            content = pickle.load(file)
            big_content.append(content)
        except EOFError:
            end_of_file = True
    for e in big_content:
        print(e)

    file.close()
    my_dict = {}

    my_dict.ge

main()
