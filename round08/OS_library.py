# Intro to programming
# Os library
# Phan viet Anh
# 256296

import os


def file_filter(file_list, extension):
    # Return a list only contains mp3 file extension
    file_list_extension = []
    for file in file_list:
        dot_position = file.find('.')
        if str(file[dot_position:]) == extension :
            file_list_extension.append(file)

    return file_list_extension


def fix_filenames(folder_name):

    file_list = os.listdir(folder_name)

    file_list_mp3 = file_filter(file_list, '.mp3')

    for file in file_list_mp3:

        file_name_in_list = file.split('-')

        character_numeric = file_name_in_list[0]

        if character_numeric.isnumeric():

            file_name_in_list.remove(file_name_in_list[0])

            dot_position = file_name_in_list[1].find('.')

            replaced_part = str(file_name_in_list[1][dot_position:])

            complete_file_name = '-' + file_name_in_list[0] + '.mp3'

            file_renamed = file_name_in_list[1].replace(
                replaced_part, complete_file_name)

            os.rename(folder_name + '/' + file,
                      folder_name + '/' + file_renamed)


def main():

    fix_filenames('OS_lib')

main()
