# Intro to programming
# Polynome
# Phan Viet Anh
# 256296

class Operand:

    def __init__(self, co_efficent, exponent):

        self.__co_efficent = co_efficent
        self.__exponent = exponent

    def get_co_efficent(self):
        return self.__co_efficent

    def get_exponent(self):
        return self.__exponent


    def set_co_efficent(self, num):
        self.__co_efficent = num

    def add(self, polynome):

        return Operand(self.__co_efficent + polynome.get_co_efficent(),
                        self.__exponent)

    def substract(self, polynome):

        return Operand(self.__co_efficent - polynome.get_co_efficent(),
                        self.__exponent)

    def multiply(self,polynome):

        return Operand(self.__co_efficent * polynome.get_co_efficent(),
                        self.__exponent + polynome.get_exponent())

    def print(self):
        if self.get_co_efficent() == 0:
            return ''
        # elif self.get_exponent()==0:
        #      return str(self.__co_efficent)
        else:
            return str(self.get_co_efficent()) + 'x^' + str(self.get_exponent())

    def print_operand(self):
        return str(self.get_co_efficent()) + 'x^' + str(self.get_exponent())

def read_file_input(prompt):
    """
    Read file and store data from file in to a list of Operand
    :param prompt: file name
    :return: a list of Operand
    """
    database = []
    try:
        filename = input(prompt)
        with open(filename, 'r') as file:
            content = file.readlines()
        for line in content:
            strings = line.rstrip().split(';')
            sub_poly = []
            for element in strings:
                poly = element.split(' ')
                operand = Operand(int(poly[0]), int(poly[1]))
                sub_poly.append(operand)
            database.append(sub_poly)

            # while True:
            #     line = file.readline().rstrip()
            #     if line == '':
            #         break
            #     strings = line.split(';')
            #     sub_poly = []
            #     for element in strings:
            #         poly = element.split(' ')
            #         operand = Operand(int(poly[0]), int(poly[1]))
            #         sub_poly.append(operand)
            #     database.append(sub_poly)
        return database
    except OSError:
        print("Error in reading the file.")


def add_command(operator1, operator2, polynomes):
    """
    Addition of two Polynome
    :param operator1: operand 1
    :param operator2: operand 2
    :param polynomes: a list of polynome
    :return:
    """
    if operator1 in range(0, len(polynomes)) and operator2 in range(0, len(polynomes)):

        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        result = [poly for poly in polynomes[operator1]]

        for index in range(len(result)):
            for polynome in polynomes[operator2]:
                if result[index].get_exponent()== polynome.get_exponent():
                    #result[index].set_number(result[index].get_number() + polynome.get_number())
                    result[index] = result[index].add(polynome)
                    break
                else:
                    if not check_polynome(polynome,result):
                        result.append(polynome)
        #simplified(result)
        print(result[0].get_co_efficent())
        print(result[1].get_co_efficent())
    else:
        print("Error: the given memory location does not exist.")


def check_polynome(polynome, result):
    """
    Checking whether an operand is or not in a list of operand
    :param polynome:
    :param result: a list of operand
    :return:
    """
    found = False
    for poly in result:
        if polynome.get_exponent() == poly.get_exponent():
            found = True
            break

    return found


def multiply_command(operator1,operator2, polynomes):
    """
    Multiply
    :param operator1:
    :param operator2:
    :param polynomes:
    :return:
    """
    result = []
    if operator1 in range(0, len(polynomes)) and operator2 in range(0, len(polynomes)):
        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        for poly in polynomes[operator1]:
            for polynome in polynomes[operator2]:
                new_poly = poly.multiply(polynome)
                if not check_polynome(new_poly,result):
                    result.append(new_poly)
                else:
                    for index in range(len(result)):
                        if result[index].get_exponent() == new_poly.get_exponent():
                            result[index].set_co_efficent(result[index].get_co_efficent()
                                                          - new_poly.get_co_efficent())
                            break
        simplified(result)
    else:
        print("Error: the given memory location does not exist.")


def substract_command(operator1,operator2, polynomes):
    if operator1 in range(0, len(polynomes)) and operator2 in range(0, len(polynomes)):
        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        result = [poly for poly in polynomes[operator1]]

        for index in range(len(result)):
            for polynome in polynomes[operator2]:
                if result[index].get_exponent() == polynome.get_exponent():
                    # result[index].set_number(result[index].get_number() + polynome.get_number())
                    result[index] = result[index].substract(polynome)
                    break
                else:
                    if not check_polynome(polynome, result):
                        polynome.set_co_efficent(0 - polynome.get_co_efficent())
                        result.append(polynome)

        simplified(result)
    else:
        print("Error: the given memory location does not exist.")

        pass


def list_polynome(polynomes):
    for index in range(len(polynomes)):
        print('Memonry location ' + str(index) + ': '
              + ' + '.join(polynome.print() for polynome in polynomes[index]))


def print_polynome(position, polynomes):
        a = sorted(polynomes[position],
                   key=lambda poly: poly.get_exponent(),
                   reverse=True)
        print('Memonry location ' + str(position) + ': '
              + ' + '.join(polynome.print_operand() for polynome in a))


        # s = ''
        # zero = 0
        # num_exponent = 0
        # #print("The simplified result: ")
        # for polynome in sorted(polynomes[position], key=lambda poly: poly.get_exponent(), reverse=True):
        #     if polynome.get_co_efficent() == 0:
        #         zero += 1
        #     if polynome.get_exponent() == 0:
        #         num_exponent += 1
        # if len(polynomes[position]) == zero:
        #     print(0)
        # elif num_exponent == 1:
        #     print('Memonry location ' + str(position) + ': '+' + '.join(str(polynome.get_co_efficent())
        #                      for polynome in sorted(polynomes[position],
        #                                             key=lambda poly: poly.get_exponent(),
        #                                             reverse=True)
        #                      if polynome.get_exponent() == 0))
        # else:
        #     print('Memonry location ' + str(position) + ': '+' + '.join(polynome.print()
        #                      for polynome in sorted(polynomes[position],
        #                                             key=lambda poly: poly.get_exponent(),
        #                                             reverse=True)
        #                      if polynome.get_co_efficent() != 0))

def simplified(result):
    s = ''
    zero = 0
    num_exponent = 0
    print("The simplified result: ")
    for polynome in sorted(result,key=lambda poly: poly.get_exponent(),reverse=True):
        if polynome.get_co_efficent() == 0:
            zero+=1
        if polynome.get_exponent() == 0:
            num_exponent += 1
    if len(result) == zero:
        print(0)
    elif num_exponent == 1:
        print(' + '.join(str(polynome.get_co_efficent())
                         for polynome in sorted(result,
                         key=lambda poly: poly.get_exponent(),
                         reverse=True)
                         if polynome.get_exponent() == 0))
    else:
        print(' + '.join(polynome.print()
                         for polynome in sorted(result,
                         key=lambda poly: poly.get_exponent(),
                         reverse=True)
                         if polynome.get_co_efficent() != 0))


def common_user_interface(database):
    while True:
        command = input('> ')

        if command == 'quit':
            print('Bye bye!')
            break

        operators = command.split(' ')
        try:

            if len(operators) !=3:
                print('Error: entry format is memory_location operation memory_location.')

            elif operators[1] not in ('+', '*', '-'):
                print("Error: unknown operator.")

            elif operators[1] == '+':
                add_command(int(operators[0]), int(operators[2]), database)

            elif operators[1] == '*':
                    multiply_command(int(operators[0]), int(operators[2]), database)
            elif operators[1] == '-':
                substract_command(int(operators[0]), int(operators[2]), database)

            else:
                pass
        except:
            print('Error: entry format is memory_location operation memory_location.')


def main():

    database = read_file_input("Enter file name: ")
    # #
    # print((database[0][0].substract(database[0][0]).print()))
    if database is not None:
        common_user_interface(database)

main()