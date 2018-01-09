# Intro to programming
# Fraction Lambda operation
# Phan viet Anh
# 256296

class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                     abs(self.__denominator))
    def get_numerator(self):
        """
        return the numerator of Fraction
        """
        return self.__numerator

    def get_denominator(self):
        """
        return the denominator of Fraction
        """
        return self.__denominator


    def simplify(self):
        """
        return the simplified form of the Fraction in the format numerator/denominator
        """
        common_divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        numerator = int(self.__numerator/common_divisor)
        denomimator = int(self.__denominator /common_divisor)

        self.__numerator = numerator
        self.__denominator = denomimator
        #
        # return "{:d}/{:d}".format(self.__numerator,
        #                              self.__denominator)

        return Fraction(self.__numerator,self.__denominator)
        # use // operator get the rounded result
        # return numerator//denominator

    def complement(self):
        """

        return the complement of Fraction in the format numerator/denominator
        """

        if self.__numerator < 0:
            return Fraction(0 - self.__numerator, self.__denominator)
        elif self.__denominator < 0:
            return Fraction(self.__numerator, 0 - self.__denominator)
        elif self.__numerator > 0 and self.__denominator > 0 :
            return Fraction(0 - self.__numerator, self.__denominator)
        else:
            return Fraction((0 - self.__numerator)*(-1), 0 - self.__denominator)

    def reciprocal(self):

        """
        return the reciprocal of Fraction in the format numerator/denominator
        """

        #self.__numerator, self.__denominator = self.__denominator, self.__numerator

        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, fract):
        """
        Multiply with another Fraction
        :param fract: another fraction
        :return: a Fraction, which is the product of multipliation
        """

        return Fraction(self.__numerator*fract.__numerator,
                        self.__denominator*fract.__denominator)

    def divide(self, fract):
        """
        Divide to another Fraction
        :param fract: another fraction
        :return: a Fractio which is the result of division
        """

        return Fraction(self.__numerator*fract.__denominator,
                        self.__denominator*fract.__numerator)

    def add(self, fract):
        """
        Addition to another fraction
        :param fract: another Fraction
        :return: a Fraction which is the summation of them
        """
        return Fraction(self.__numerator*fract.__denominator
                        + self.__denominator*fract.__numerator,
                        self.__denominator*fract.__denominator)

    def deduct(self, fract):
        """
        the difference between one fraction and another Fraction
        :param fract: another Fraction
        :return: a Fraction which is the different value between those
        """

        if self.__numerator * fract.__denominator > self.__denominator * fract.__numerator:

            numer = self.__numerator * fract.__denominator \
                    - self.__denominator * fract.__numerator
            deno = self.__denominator * fract.__denominator

            self.__numerator = numer
            self.__denominator = deno

            return Fraction(self.__numerator,
                            self.__denominator)
        else:

            numer = self.__denominator * fract.__numerator \
                    - self.__numerator * fract.__denominator
            deno = self.__denominator * fract.__denominator

            self.__numerator = numer
            self.__denominator = deno

            return Fraction(self.__numerator,
                            self.__denominator)

    def __lt__(self, other):
        """
        Compare two fractions and return the boolean values for the less one
        :param other: another fraction
        :return: Bool value
        """
        if self.__numerator * other.__denominator - other.__numerator * self.__denominator < 0:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Compare two fractions and return the boolean values for the greater one
        :param other: another fraction
        :return: Bool value
        """
        if self.__numerator * other.__denominator - other.__numerator * self.__denominator > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def add(fract, dict, name):

    try:
        num_deno = fract.split('/')
        numerator, denominator = int(num_deno[0]), int(num_deno[1])
        dict[name] = Fraction(numerator, denominator)
    except:
        print('Error input!')

def print_dict(dict):
    name = input('Enter a name: ')
    if name in dict:
        print(name + ' = ' + dict[name].return_string())
    else:
        print('Name ' + name + ' was not found')

def list_dict(dict):
    if len(dict) > 0:
        for key in sorted(dict):
            print(key, dict[key], sep=' = ')


def multiply_dict(dict):

    operand_1 = input('1st operand: ')
    if operand_1 not in dict:
        print('Name ' + operand_1 + ' was not found')
    else:
        operand_2 = input('2nd operand: ')

        if operand_2 not in dict:
            print('Name ' + operand_2 + ' was not found')
        else:
            product = dict[operand_1].multiply(dict[operand_2])
            print(dict[operand_1].return_string() + ' * ' + dict[operand_2].return_string(), product, sep=' = ' )
            print('simplified ' + product.simplify().return_string())


def command_line_user_interface(dict):
    # while True:
    #     command = input("> ")
    #
    #     if command == "add":
    #         fraction = input('Enter a fraction in the form integer/integer: ')
    #         name = input('Enter a name: ')
    #         add(fraction, dict, name)
    #
    #     elif command == "print":
    #         print_dict(dict)
    #
    #     elif command == "*":
    #         multiply_dict(dict)
    #
    #     elif command == "list":
    #         list_dict(dict)
    #
    #     elif command == 'quit':
    #         print('Bye bye!')
    #         break
    #
    #     else:
    #         print("Unknown command!")

    # Testing Lambda function with dictionary name

    #

    while True:
        command = input("> ")

        if command == "add":
            fraction = input('Enter a fraction in the form integer/integer: ')
            name = input('Enter a name: ')

        if command in dict:
            result = dict[command]

        elif command == 'quit':
            print('Bye bye!')
            break

        else:
            print("Unknown command!")


def main():

    fraction_dict = {}

    command_line_user_interface(fraction_dict)

main()
