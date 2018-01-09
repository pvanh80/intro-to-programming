# Intro to programming
# Classes and Objects
# Phan Viet Anh
# 256296


import cellphone


def main():

    man = input('What is your phone\'s manufacture? ')
    mod = input('What is your phone\'s model? ')
    price = float(input('What is your phone\'s price? '))
    cellphone = cellphone.CellPhone(man, mod, price)

    #print(cellphone)

main()
