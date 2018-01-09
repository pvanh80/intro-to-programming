# Intro to programming
# Numbering the file rows Does not succeed
# Phan viet Anh
# 256296


def main():

    try:

        file_open = open(input('Enter the name of the file: '), 'r')

        file_content = file_open.readline()

        line_number = 1
        while file_content != '':

            print(format(line_number, '1,.0f') + ' ' + file_content.rstrip('\n'))

            line_number += 1

            file_content = file_open.readline()

        file_open.close()

    except:

        print('There was an error in reading the file.')


main()
