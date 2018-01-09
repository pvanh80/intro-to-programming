# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: accesscontrol, program code template
# Phan Viet Anh
# 256296
# Note: for submission

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.
        :param id: card holders personal id (str)
        :param name: card holders name (str)

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """
        # TODO: Implement the constructor
        pass
        self.__id = id
        self.__name = name

        self.__access = []


    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        code_printed = []
        if len(self.get_access()) == 0:
            code_printed.append('')
        else:
            for code in self.get_access():
                if code in area_list(DOORCODES):
                    code_printed.append(code)
                else:

                    if len(DOORCODES[code]) == 0:
                        code_printed.append(code)
                    else:
                        for code_added in DOORCODES[code]:
                            if code_added in self.get_access():
                                pass
                                break
                                # code_printed.append(code_added)
                            else:
                                code_printed.append(code)

        print(self.get_id() + ', ' + self.get_name() + ', ' + 'access: '
              + ', '.join(code for code in sorted(code_printed)))

        pass # TODO: Implement the method

    def get_name(self):
        """
        Get the name of card holder
        :return: Returns the name of the accesscard holder.
        """

        return self.__name

    # implement get_id for access class

    def get_id(self):
        """
        Get the id of card holder
        :return: return the id of accesscard holder
        """
        return self.__id

    def get_access(self):
        """
        Getting access right of card holder
        :return: return access right of accesscard holder
        """

        return self.__access

    def set_access(self, accesscodes):
        """
        Set access right to card holder
        :param accesscodes: a list of access right
        :return:
        """

        self.__access = accesscodes

    pass  # TODO: Implement the method

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.
        :param new_access_code: The accesscode to be added in the card.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        if new_access_code in DOORCODES.keys():
            if new_access_code not in self.get_access():
                if len(DOORCODES[new_access_code])!=0:
                    for code in DOORCODES[new_access_code]:
                        if code not in self.get_access():
                            self.__access.append(new_access_code)
                            break
                        else:
                            pass
                else:
                    self.__access.append(new_access_code)
            else:
                pass

        elif new_access_code in area_list(DOORCODES):

            if new_access_code in self.get_access():
                pass
            else:
                self.__access.append(new_access_code)

        else:
            pass

        pass  # TODO: Implement the method

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.
        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        if door in DOORCODES.keys():
            if len(self.get_access()) == 0:
                return door in self.get_access()
            elif door in self.get_access():
                return door in self.get_access()

            else:
                for code in DOORCODES[door]:
                    if code in self.get_access():
                        return code in DOORCODES[door]
                        break
                    else:
                        return code in DOORCODES

        else:
            return door in DOORCODES


    pass  # TODO: Implement the method

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: The accesscard whose access rights are added to this card.
        :return:
        """
        for code in card.get_access():
            self.add_access(code)
        pass # TODO: Implement the method
        return self.__access


def list_data_info(data):
    """
    Print out list of accesscard holder
    :param data: a lis of accesscard holder
    :return:
    """

    for card in sorted(data, key=lambda card: card.get_id()):
        card.info()


def checking_card_id(card_id, data):
    """
    Checking card id is exist in the data list or not
    :param card_id: id of card holder
    :param data: list of card holder
    :return: boolean value which id is found in the list
    """
    found = True
    for card in data:
        if card_id == card.get_id():
            return found
            break
    if not found:
        return found


def info_command(card_id, data):
    """
    Print out info of accesscard holder with card id
    :param card_id: id of card holder
    :param data: list of card holders
    :return:
    """
    if checking_card_id(card_id,data):
        for card in data:
            if card_id == card.get_id():
                card.info()
                break
    else:
        print("Error: unknown id.")


def access_command(card_id, door_id, data):
    """
    Print out whether a card holder is allowed to access the door or not
    :param card_id: id of card holder
    :param door_id: doorcode
    :param data: list of card holders
    :return:
    """

    if not checking_card_id(card_id,data):
        print("Error: unknown id.")
    elif door_id not in DOORCODES:
        print('Error: unknown doorcode.')

    elif get_card_holder_info(card_id, data, info='access').check_access(door_id) == True:
        print('Card ' + card_id + ' ( '
              + get_card_holder_info(card_id, data, info='name')
              + ' )' + ' has access to door ' + door_id)
    else:
        print('Card ' + card_id + ' ( '
              + get_card_holder_info(card_id, data, info='name')
              + ' )' + ' has no access to door ' + door_id)


def get_card_holder_info(card_id, data, info='access'):
    """
    Get accesscard holder with card id and data
    :param card_id: id of card holder
    :param data: list if card holders
    :param info: access or name which info
    :return: card holder if info='access' and name of card holder if info='name'
    """

    if info=='access' or '':
        for card in data:
            if card_id == card.get_id():
                return card # return object in data_list
                break
    elif info=='name':
        for card in data:
            if card_id == card.get_id():
                return card.get_name()
                break
    else:
        return None


def add_command(card_id, access_code, data):
    """
    Adding access right to specific card holder
    :param card_id:
    :param access_code:
    :param data:
    :return:
    """

    if not checking_card_id(card_id,data):
        print('Error: unknown id.')
    elif access_code not in DOORCODES.keys() \
            and access_code not in area_list(DOORCODES):
        print('Error: unknown accesscode.')

    else:

        get_card_holder_info(card_id, data, info='access').add_access(access_code)


def merge_command(card_id_to, card_id_from, data):
    """
    Merging the access right from one card holder to another
    :param card_id_to: id of a access card holder
    :param card_id_from: id of another card holder
    :param data: list of card holders
    :return:
    """
    if not checking_card_id(card_id_to,data) \
            or not checking_card_id(card_id_from,data):
        print('Error: unknown id.')
    else:
        get_card_holder_info(card_id_to,data,info='access').merge(
            get_card_holder_info(card_id_from,data,info='access'))


def area_list(dicta):
    """
    List of areacodes belongs to
    :param dicta: list of card holders
    :return:
    """
    areacode = []
    for area in dicta.values():
      for code in area:
        if code not in areacode:
          areacode.append(code)
    return areacode


def main():
    # TODO: Implement the reading of the inputfile and storing the information.

    data = []  # store accesscard list >> should be save as a dict with key and value

    card_holder = ''  # end of file

    try:

        file_input = open('accessinfo.txt', 'r')

        while True:

            card_holder = file_input.readline().rstrip('\n')

            if card_holder == '':
                break
            card_info = card_holder.split(';')
            card = Accesscard(card_info[0], card_info[1])
            if len(card_info[2]) != 0:
                access_right = card_info[2].split(',')
                card.set_access(access_right)
                data.append(card)
            else:
                access_right = []
                card.set_access(access_right)
                data.append(card)

    except:
        print('Error: file cannot be read.')

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            pass # TODO: Excecute the command list here
            list_data_info(data)

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            pass  # TODO: Excecute the command info here
            info_command(card_id, data)

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            pass  # TODO: Excecute the command access here
            access_command(card_id, door_id, data)

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            pass  # TODO: Excecute the command add here
            add_command(card_id, access_code, data)
        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            pass  # TODO: Excecute the command merge here
            merge_command(card_id_to, card_id_from, data)
        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")

main()
