# intro to programming
# CSV lib
# Phan Viet Anh
# 256296

import csv


def main():

    try:
        converted = False
        file_name = input("Enter the name of the input file: ")
        dialect_class =input("and its dialect: ")
        file_converted =input('Enter the name of the output file: ')
        dialect_class_converted =input('and its dialect: ')

        if dialect_class not in ("excel", "unix", "excel-tab"):
            print("\nThe given dialect is wrong.")
        elif dialect_class_converted not in ("excel", "unix", "excel-tab"):
            print("\nThe given dialect is wrong.")
        else:
            try:

                f = open(file_name, 'r', newline='')
                reader = csv.reader(f, dialect=dialect_class)

                f_con = open(file_converted, 'a', newline='')
                writer = csv.writer(f_con, dialect=dialect_class_converted)

                for row in reader:
                    writer.writerow(row)
                converted = True
            except :

                print("\nThere was an error in handling the file.")

            # dialects Unix : delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL

            if converted == True:
                print('\nFile '+ file_name + ' has been converted into '+ dialect_class_converted +'.')
    except csv.Error as e:
        print("Error in processing the file.")

main()
