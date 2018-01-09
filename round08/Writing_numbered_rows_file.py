# Intro to programming
# Writing numbered rows to a file
# Phan viet Anh
# 256296


def main():

    file_name = input('Enter the name of the file: ')
    file_open = open(file_name, 'w')
    print('Enter rows of text. Quit by entering an empty row.')
    row = 1
    while True:

        file_line = input("")

        if file_line == '':
            break

        row_num = str(row)
        file_open.write(row_num + ' ' + file_line + '\n')

        row += 1

    file_open.close()
    print("File " + file_name + " has been written.")

main()
