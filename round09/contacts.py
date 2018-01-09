# intro to programming
# Contacts
# Phan Viet Anh
# 256296


def read_file(file_name):
    file_content = {}
    dict_values = {}

    file = open(file_name,'r')
    row_tittle = file.readline()
    title = row_tittle.rstrip('\n')

    while True:
        row = file.readline()
        row_content = row.rstrip('\n')
        if row_content == '':
            break

        field = row_content.split(';')
        dict_values['name'] = field[1]
        dict_values['phone'] = field[2]
        dict_values['email'] = field[3]
        dict_values['skype'] = field[4]
        file_content[field[0]] = dict_values

        dict_values = {}
    file.close()
    return file_content

