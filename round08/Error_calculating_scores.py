# Intro to programming
# Calculating scores
# Phan viet Anh
# 256296


def main():

    score = {}

    file_name = input('Enter the name of the score file: ')
    try:
        file_open = open(file_name, 'r')
        row = file_open.readline()

    except :
        print('There was an error in reading the file.')

    else:

        while row != '':

            space_position = row.find(' ')
            if space_position == -1 :
                print('There was an erroneous line in the file:')
                print(row)
                break
            else:
                try:
                    int(row[space_position + 1:])
                except:
                    print('There was an erroneous score in the file:')
                    print(row[space_position + 1:])
                    break
                else:

                    if row[:space_position] in score:
                        score_update = int(row[space_position + 1:]) + int(score[row[:space_position]])
                        score[row[:space_position]] = score_update
                    else:
                        score[row[:space_position]] = int(row[space_position + 1:])
                    row = file_open.readline().rstrip('\n')

            if row == '':
                print('Contestant score:')
                for key in sorted(score):
                    print(key, score[key], sep=' ')

        file_open.close()

main()
