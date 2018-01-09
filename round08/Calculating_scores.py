# Intro to programming
# Calculating scores
# Phan viet Anh
# 256296


def main():

    score = {}

    file_name = input('Enter the name of the score file: ')
    file_open = open(file_name, 'r')
    row = file_open.readline()

    while row != '':

        space_position = row.find(' ')
        if row[:space_position] in score:
            score_update = int(row[space_position + 1:]) + int(score[row[:space_position]])
            score[row[:space_position]] = score_update
        else:
            score[row[:space_position]] = int(row[space_position + 1:])
        row = file_open.readline().rstrip('\n')

    file_open.close()
    print('Contestant score:')
    for key in sorted(score):
        print(key, score[key], sep=' ')


main()