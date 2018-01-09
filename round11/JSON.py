# intro to programming
# JSON TO CSV
# Phan Viet Anh
# 256296


import json


def main():
    converted = False
    try:

        input_file = input("Enter the name of the input file: ")
        output_file = input("Enter the name of the output file: ")

        f = open(input_file,'r')
        reader = json.load(f)

        f_con = open(output_file,'a', newline='')
        for row in reader:

            f_con.write(row["stationId"] + ';' + row["name"] + '\n')

        f.close()
        f_con.close()

        converted = True
    except :
        print("\nThere was an error in handling the file.")

    if converted == True:
        print('\nConversion succeeded.')

main()
