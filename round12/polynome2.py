# Intro to programming
# Polynome
# Phan Viet Anh
# 256296

class Operand:

    def __init__(self, number, co_efficent):

        self.__number = number
        self.__co_efficent = co_efficent

    def get_number(self):
        return self.__number

    def get_coefficent(self):
        return self.__co_efficent


    def set_number(self, num):
        self.__number = num

    def add(self, polynome):

        return Operand(self.__number + polynome.get_number(),
                        self.__co_efficent)

    def substract(self, polynome):

        return Operand(self.__number - polynome.get_number(),
                        self.__co_efficent)

    def multiply(self,polynome):

        return Operand(self.__number * polynome.get_number(),
                        self.__co_efficent + polynome.get_coefficent())

    def print(self):
        if self.get_number() == 0:
            return str(0)
        # elif self.get_coefficent()==0:
        #     return str(self.get_number())
        else:
            return str(self.get_number()) + 'x^' + str(self.get_coefficent())

class Polynome:
    """
    class Polynome with private property is a list of operands which exponents and
    coefficents stored in another list
    ie. polynome: 5x^4 + 3x^2 will be like [[5 4], [3, 2]]
    """
    def __init__(self, polynome):
        self.__polynome = polynome

    def get_polynome(self):
        return self.__polynome

    def add(self, polynome):
        for index in range(len(result)):
            for polynome in polynomes[operator2]:
                if result[index].get_coefficent()== polynome.get_coefficent():
                    #result[index].set_number(result[index].get_number() + polynome.get_number())
                    result[index] = result[index].add(polynome)
                    break
                else:
                    if not check_polynome(polynome,result):
                        result.append(polynome)



def read_file_input(prompt):
    database = []
    try:
        filename = input(prompt)
        with open(filename, 'r') as file:
            while True:
                line = file.readline().rstrip()
                if line == '':
                    break
                strings = line.split(';')
                sub_poly = []
                for element in strings:
                    poly = element.split(' ')
                    operand = Operand(int(poly[0]), int(poly[1]))
                    sub_poly.append(operand)
                database.append(Polynome(sub_poly))
        return database
    except OSError:
        print("Error in reading the file.")


def add_command(operator1, operator2, polynomes):
    if operator1 in range(0,7) and operator2 in range(0, 7):

        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        result = [poly for poly in polynomes[operator1]]

        for index in range(len(result)):
            for polynome in polynomes[operator2]:
                if result[index].get_coefficent()== polynome.get_coefficent():
                    #result[index].set_number(result[index].get_number() + polynome.get_number())
                    result[index] = result[index].add(polynome)
                    break
                else:
                    if not check_polynome(polynome,result):
                        result.append(polynome)
        simplified(result)
    else:
        print("Error: the given memory location does not exist.")




def check_polynome(polynome, result):
    found = False
    for poly in result:
        if polynome.get_coefficent() == poly.get_coefficent():
            found = True
            break

    return found


def multiply_command(operator1,operator2, polynomes):
    result = []
    if operator1 in range(0, 7) and operator2 in range(0, 7):
        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        for poly in polynomes[operator1]:
            for polynome in polynomes[operator2]:
                new_poly = poly.multiply(polynome)
                if not check_polynome(new_poly,result):
                    result.append(new_poly)
                else:
                    for index in range(len(result)):
                        if result[index].get_coefficent() == new_poly.get_coefficent():
                            result[index].set_number(result[index].get_number() - new_poly.get_number())
                            break
        simplified(result)
    else:
        print("Error: the given memory location does not exist.")


def substract_command(operator1,operator2, polynomes):
    if operator1 in range(0, 7) and operator2 in range(0, 7):
        print_polynome(operator1, polynomes)
        print_polynome(operator2, polynomes)

        result = [poly for poly in polynomes[operator1]]

        for index in range(len(result)):
            for polynome in polynomes[operator2]:
                if result[index].get_coefficent() == polynome.get_coefficent():
                    # result[index].set_number(result[index].get_number() + polynome.get_number())
                    result[index] = result[index].substract(polynome)
                    break
                else:
                    if not check_polynome(polynome, result):
                        polynome.set_number(0 - polynome.get_number())
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
        a = sorted(polynomes[position], key=lambda poly: poly.get_coefficent(), reverse=True)
        print('Memonry location ' + str(position) + ': '
              + ' + '.join(polynome.print() for polynome in a))


def simplified(result):
    print("The simplified result: ")
    print(' + '.join(polynome.print()
                     for polynome in sorted(result,
                                            key=lambda poly: poly.get_coefficent(),
                                            reverse=True) if polynome.get_number() !=0) )


def common_user_interface(polynomes):
    while True:
        command = input('> ')

        if command == 'quit':
            print('Bye bye!')
            break

        operators = command.split(' ')

        if len(operators) !=3:
            print('Error: entry format is memory_location operation memory_location.')

        elif operators[1] not in ('+', '*', '-'):
            print("Error: unknown operator.")

        elif operators[1] == '+':
            add_command(int(operators[0]), int(operators[2]), polynomes)

        elif operators[1] == '*':
                multiply_command(int(operators[0]), int(operators[2]), polynomes)
        elif operators[1] == '-':
            substract_command(int(operators[0]), int(operators[2]), polynomes)

        else:
            pass
def main():

    database = read_file_input("Enter file name: ")
    print(database[0].get_polynome())
    # if polynomes is not None:
    #     common_user_interface(polynomes)

main()
